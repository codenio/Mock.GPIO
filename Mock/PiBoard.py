from threading import ThreadError
import threading
import time
import socket as sk
#from GPIO.py import GPIO


class Board:
    channelConfigs = {}
    channelEvents = {}
    gpio_direction = {}
    __instance = None
    serviceThread = None
    outFile = "/tmp/PiBoard.out"
    pin_to_gpio_rev1 = {-1, -1, -1, 0, -1, 1, -1, 4, 14, -1, 15, 17, 18, 21, -1, 22, 23, -1, 24, 10, -1, 9, 25, 11, 8, -1, 7, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1 }
    pin_to_gpio_rev2 = {-1, -1, -1, 2, -1, 3, -1, 4, 14, -1, 15, 17, 18, 27, -1, 22, 23, -1, 24, 10, -1, 9, 25, 11, 8, -1, 7, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1 }
    pin_to_gpio_rev3 = {-1, -1, -1, 2, -1, 3, -1, 4, 14, -1, 15, 17, 18, 27, -1, 22, 23, -1, 24, 10, -1, 9, 25, 11, 8, -1, 7, -1, -1, 5, -1, 6, 12, 13, -1, 19, 16, 26, 20, -1, 21 }


    @staticmethod
    def getInstance():
        """ Static access method. """
        if Board.__instance == None:
            Board()
        return Board.__instance

    def __init__(self):
#	print('__init__')
        if Board.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            Board.__instance = self

            i = 0
            while i < 54:
                Board.__instance.gpio_direction[i] = -1
                i += 1
        '''
        if Board.__instance.rpiinfo.p1_revision == 1:
            Board.__instance.pin_to_gpio = Board.__instance.pin_to_gpio_rev1
        elif Board.__instance.rpiinfo.p1_revision == 2:
            Board.__instance.pin_to_gpio = Board.__instance.pin_to_gpio_rev2
        else # assume model B+ or A+ or 2B
        '''
        # Based on GPIO.RPI_REVISION = 3
        Board.__instance.pin_to_gpio = Board.__instance.pin_to_gpio_rev3

        Board.__instance.serviceThread = ServiceThread()
        Board.__instance.serviceThread.setPiBoardCallback(Board.__instance.piBoardCallback)
        Board.__instance.serviceThread.threadify()

    def piBoardCallback(_piBoardInstance, _value):
        v=_value.decode("UTF-8")
        print('piBoardCallback: ' + v)
        global channelEvents
        # This assumes that _value is in format {channel:[HI|LOW]}, i.e. 22:HI
        values = v.split(":")
        print('-'+ str(values[0])+'-' )
        tmpV=values[0]
        print("tmpV: -" + tmpV + "-")
        channel = int(tmpV)
        edge = values[1]

        _dir = Board.__instance.gpio_direction[int(channel)]

        if not _dir == -1 and  not _dir == 1:
            raise ValueError("Wrong direction for " + channel)

        edge_dec = -1
        print('edge: -'+edge.rstrip() + '-' )
        if edge.rstrip() == "LOW":
            edge_dec = 0
        elif edge.rstrip() == "HI":
            edge_dec = 1
        else:
            raise ValueError("Edge must be either HI or LOW")

        event = _piBoardInstance.channelEvents[int(channel)]
        cc = _piBoardInstance.channelConfigs[int(channel)]
        # TODO: Handle logic on wether to call event callback or not.
        if not int(cc.current) == edge_dec:
            cc.current = edge_dec
            _piBoardInstance.channelConfigs[int(channel)] = cc
            event.eventCallback(event.channel)

    def setChannelConfig(_piBoardInstance, channel):
        if channel != None:
            _piBoardInstance.channelConfigs[channel.chanel] = channel

    def setChannelEvent(_piBoardInstance, _channel, _edge, _channelEventCallback):

        if _channel != None:
            event = Event(_edge, _channelEventCallback, _channel)
            _piBoardInstance.channelEvents[_channel] = event

    def cleanUp(__X):
        if len(Board.__instance.channelEvents) == 0 and len(Board.__instance.channelConfigs):
            t = Board.__instance.serviceThread.thread
            print('t: ' + str(t))
            if t == None:
                exit()
            currThreadIdent = t.ident()
            currThreadIdent = currThreadIdent + "kill"
            t1 = thread_with_exception('Thread 1')
            t1.start()
            time.sleep(2)
            t1.raise_exception()
            t1.join()
            if Board.__instance.serviceThread.thread.is_alive():
                raise ThreadError("Failed to stop " + currThreadIdent)

    def logToFile(_piBoardInstance,_channel,_value):
        with open(_piBoardInstance.outFile, 'a') as f:
			loggMsg = "event:" + str(Board.__instance) + ":" +str(_channel) + ":" + str(_value) + "\n"
			print(loggMsg)
            f.write(loggMsg)
            f.close()


class Event:

    eventCallback = None
    edge = None
    channel = None

    def __init__(self, _edge, _eventCallback, _channel):
        self.eventCallback = _eventCallback
        self.edge = _edge
        self.channel = _channel


class Service:

    serviceThreadCallback = None

    def __init__(self):
        print(self)

    def listen(self, _serviceThreadCallback):
        global serviceThreadCallback
        serviceThreadCallback = _serviceThreadCallback
        connection = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
        connection.setsockopt(sk.SOL_SOCKET, sk.SO_REUSEADDR, 1)
        try:
            connection.bind(('0.0.0.0', 5566))
        except sk.error:
            print('sk.error - return 0')
            return 0
        connection.listen(10)
        while True:
            current_connection, address = connection.accept()
            while True:
                data = current_connection.recv(2048)

                if data == 'quit\\n':
                    current_connection.shutdown(1)
                    current_connection.close()
                    break

                elif data == 'stop\\n':
                    current_connection.shutdown(1)
                    current_connection.close()
                    exit()

                elif data:
                    _serviceThreadCallback(data)

                else:
                    break

    def setCallback(_serviceThreadCallback):
        global serviceThreadCallback
        serviceThreadCallback = _serviceThreadCallback


class ServiceThread:

    thread = None
    svc = None
    piBoardCallback = None

    def __init__(self, interval=1):
        self.interval = interval

    def run(self):
            global piBoardCallback
            self.svc = Service()
            self.svc.listen(piBoardCallback)

    def setPiBoardCallback(_serviceThread, _piBoardCallback):
        global piBoardCallback
        piBoardCallback = _piBoardCallback

    def threadify(self):
        global thread
        thread = threading.Thread(target=self.run)
        thread.daemon = True  # Daemonize thread
        thread.start()  # Start the execution


def ext_callback(_event):
    print("ext_callback")
    print(__event.channel)
    print(_event.edge)
    print(_event.eventCallback)




### Only for testing


def getBoard():
    _rpib = Board.getInstance()
    if _rpib == None:
        _rpib = Board()
    return _rpib

class Channel:
    def __init__(self,channel, direction, initial=0,pull_up_down=0):
        self.chanel = channel
        self.direction = direction
        self.initial = initial
        self.current = initial
        self.pull_up_down = pull_up_down


if __name__ == '__main__':

    try:
        while True:

#             GPIO.setmode(GPIO.BCM)
#             GPIO.setup(22, GPIO.IN, 0, GPIO.PUD_UP)
#             GPIO.add_event_detect(22, GPIO.FALLING, ext_callback, bouncetime=1500)


            rpib = getBoard()
#             rpib.setChannelConfig(Channel(22, 32, 0, 0))
#             rpib.setChannelEvent(22, 32, ext_callback)
            rpib.logToFile(22, GPIO.HIGH)
#             time.sleep(1000)
            #rpib.cleanUp()
    except KeyboardInterrupt:
        pass
