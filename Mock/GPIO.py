#Mock Library for RPi.GPIO


import logging
import os
import time
import types
# import yaml

from RPi import PiBoard

logger = logging.getLogger(__name__)

log_level = os.getenv('LOG_LEVEL')

if log_level is not None:
    if log_level == "Info":
        logger.setLevel(logging.INFO)
    if log_level == "Debug":
        logger.setLevel(logging.DEBUG)
    if log_level == "Warning":
        logger.setLevel(logging.WARNING)
    if log_level == "Error":
        logger.setLevel(logging.ERROR)
    if log_level == "Critical":
        logger.setLevel(logging.CRITICAL)
else:
    logger.setLevel(logging.ERROR)

stream_formatter = logging.Formatter('%(asctime)s:%(levelname)s: %(message)s')
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(stream_formatter)
logger.addHandler(stream_handler)

BCM = 11
BOARD = 10
BOTH = 33
FALLING = 32
HARD_PWM = 43
HIGH = 1
I2C = 42
IN = 1
LOW = 0
OUT = 0
INPUT = 1
PUD_DOWN = 21
PUD_OFF = 20
PUD_UP = 22
RISING = 31
RPI_INFO = {'MANUFACTURER': 'Sony', 'P1_REVISION': 3, 'PROCESSOR': 'BCM2837', 'RAM': '1G', 'REVISION': 'a020d3', 'TYPE': 'Pi 3 Model B+'}
RPI_REVISION = 3
SERIAL = 40
SPI = 41
UNKNOWN = -1
VERSION = '0.7.0'
PY_EVENT_CONST_OFFSET = 30

BCM2708_PERI_BASE_DEFAULT = 0x20000000
BCM2709_PERI_BASE_DEFAULT = 0x3f000000
GPIO_BASE_OFFSET = 0x200000
FSEL_OFFSET = 0  # 0x0000
SET_OFFSET = 7  # 0x001c / 4
CLR_OFFSET = 10  # 0x0028 / 4
PINLEVEL_OFFSET = 13  # 0x0034 / 4
EVENT_DETECT_OFFSET = 16  # 0x0040 / 4
RISING_ED_OFFSET = 19  # 0x004c / 4
FALLING_ED_OFFSET = 22  # 0x0058 / 4
HIGH_DETECT_OFFSET = 25  # 0x0064 / 4
LOW_DETECT_OFFSET = 28  # 0x0070 / 4
PULLUPDN_OFFSET = 37  # 0x0094 / 4
PULLUPDNCLK_OFFSET = 38  # 0x0098 / 4
PULLUPDN_OFFSET_2711_0 = 57
PULLUPDN_OFFSET_2711_1 = 58
PULLUPDN_OFFSET_2711_2 = 59
PULLUPDN_OFFSET_2711_3 = 60

NO_EDGE      = 0
RISING_EDGE  = 1
FALLING_EDGE = 2
BOTH_EDGE    = 3
_mode = 0

channel_config = {}

#flags
setModeDone = False

class Channel:
    def __init__(self,channel, direction, initial=0,pull_up_down=PUD_OFF):
        self.chanel = channel
        self.direction = direction
        self.initial = initial
        self.current = initial
        self.pull_up_down = pull_up_down


#GPIO LIBRARY Functions
def setmode(mode):
    """
    Set up numbering mode to use for channels.
    BOARD - Use Raspberry Pi board numbers
    BCM   - Use Broadcom GPIO 00..nn numbers
    """
    
    board = getBoard()
    
    # GPIO = GPIO()
    time.sleep(1)
    if(mode == BCM):
        setModeDone = True
        _mode = mode

    elif (mode == BOARD):
        setModeDone = True
    else:
        setModeDone = False

def getmode():
    """
    Get numbering mode used for channel numbers.
    Returns BOARD, BCM or None
    """
    board = getBoard()
    return _mode

def setwarnings(flag):
    """
    Enable or disable warning messages
    """
    board = getBoard()
    logger.info("Set Warings as {}".format(flag))

def setup(channel, direction, initial=0,pull_up_down=PUD_OFF):
    """
    Set up a GPIO channel or list of channels with a direction and (optional) pull/up down control
    channel        - either board pin number or BCM number depending on which mode is set.
    direction      - IN or OUT
    [pull_up_down] - PUD_OFF (default), PUD_UP or PUD_DOWN
    [initial]      - Initial value for an output channel

    """
    logger.info("setup channel : {} as {} with intial :{} and pull_up_dowm {}".format(channel,direction,initial,pull_up_down))
    board = getBoard()
    global channel_config
    
    if isinstance(channel, list):
        print("channel is list")
        for c in channel:
            print ("processing channel " + str(c)) 
            channel_config[c] = Channel(c, direction, initial, pull_up_down)
            board.setChannelConfig(channel_config[c])
            board.gpio_direction[c] = direction   
    elif isinstance(channel, int):
        print("channel is int")
        channel_config[channel] = Channel(channel, direction, initial, pull_up_down)
        board.setChannelConfig(channel_config[channel])
        board.gpio_direction[channel] = direction
    else:
        raise TypeError("channel is of wrong type: " + channel )    
    
    

def output(channel, value):
    """
    Output to a GPIO channel or list of channels
    channel - either board pin number or BCM number depending on which mode is set.
    value   - 0/1 or False/True or LOW/HIGH

    """
    board = getBoard()
    board.logToFile(channel,value)
    logger.info("output channel : {} with value : {}".format(channel, value))

def input(channel):
    """
    Input from a GPIO channel.  Returns HIGH=1=True or LOW=0=False
    channel - either board pin number or BCM number depending on which mode is set.
    """
    board = getBoard()
    logger.info("reading from chanel {}".format(channel))

def wait_for_edge(channel,edge,bouncetime,timeout):
    """
    Wait for an edge.  Returns the channel number or None on timeout.
    channel      - either board pin number or BCM number depending on which mode is set.
    edge         - RISING, FALLING or BOTH
    [bouncetime] - time allowed between calls to allow for switchbounce
    [timeout]    - timeout in ms
    """
    board = getBoard()
   
    _gpio 
#    unsigned int gpio;
#    int channel, edge, result;
    _channel
    _edge
#    bouncetime = -666; // None
    _bouncetime = None
#    int timeout = -1; // None
    _timeout = None

#     static char *kwlist[] = {"channel", "edge", "bouncetime", "timeout", None}
    _kwlist = {}
    _kwlist[0] = "channel"
    _kwlist[1] = "edge"
    _kwlist[2] = "bouncetime"
    _kwlist[3] = "timeout"
    _kwlist[4] = None

    if not PyArg_ParseTupleAndKeywords(args, _kwargs, "ii|ii", _kwlist, _channel, _edge, _bouncetime, _timeout):
        return None
    
    # TODO verify this
    _get_gpio_numbers = get_gpio_number(_channel, _gpio).split(":")
    _gpio = int(_get_gpio_numbers[1])
    if int(_get_gpio_numbers[0]) == 0:
        return None

#     check channel is setup as an input
    
    if not board.gpio_direction[_gpio] == INPUT:
        raise RuntimeError("You must setup() the GPIO channel as an input first")
        return None

#    // is edge a valid value?
    _edge -= PY_EVENT_CONST_OFFSET
    if not _edge == RISING_EDGE and not _edge == FALLING_EDGE and _edge == BOTH_EDGE:
        raise ValueError("The edge must be set to RISING, FALLING or BOTH")
        return None

    if _bouncetime <= 0 and not _bouncetime == None:
        raise ValueError("Bouncetime must be greater than 0")
        return None

    if _timeout <= 0 and not _timeout != None:
        raise ValueError("Timeout must be greater than 0")
        return None
    
    if _result == 0:
        return None
    elif _result == -1:
        raise RuntimeError("Conflicting edge detection events already exist for this GPIO channel")
        return None
    elif _result == -2:
        raise RuntimeError("Error waiting for edge")
        return None
    else:
        return Py_BuildValue("i", _channel)
    
    logger.info("waiting for edge : {} on channel : {} with bounce time : {} and Timeout :{}".format(edge,channel,bouncetime,timeout))


def add_event_detect(channel,edge,callback,bouncetime):
    """
    Enable edge detection events for a particular GPIO channel.
    channel      - either board pin number or BCM number depending on which mode is set.
    edge         - RISING, FALLING or BOTH
    [callback]   - A callback function for the event (optional)
    [bouncetime] - Switch bounce timeout in ms for callback
    """
    getBoard().setChannelEvent(channel, edge, callback)
    logger.info("Event detect added for edge : {} on channel : {} with bouce time : {} and callback {}".format(edge,channel,bouncetime,callback))

def event_detected(channel):
    """
    Returns True if an edge has occurred on a given GPIO.  You need to enable edge detection using add_event_detect() first.
    channel - either board pin number or BCM number depending on which mode is set.
    """
    board = getBoard()
    logger.info("Waiting for even detection on channel :{}".format(channel))

def add_event_callback(channel,callback):
    """
    Add a callback for an event already defined using add_event_detect()
    channel      - either board pin number or BCM number depending on which mode is set.
    callback     - a callback function
    """
    logger.info("Event Calback : {} added for channel : {}".format(callback,channel))

def remove_event_detect(channel):
    """
    Remove edge detection for a particular GPIO channel
    channel - either board pin number or BCM number depending on which mode is set.
    """
    board = getBoard()
    logger.info("Event Detect Removed for channel : {}".format(channel))

def gpio_function(channel):
    """
    Return the current GPIO function (IN, OUT, PWM, SERIAL, I2C, SPI)
    channel - either board pin number or BCM number depending on which mode is set.
    """
    board = getBoard()
    logger.info("GPIO function of Channel : {} is {}".format(channel,channel_config[channel].direction))


class PWM:
    # initialise PWM channel
    def __init__(self, channel, frequency):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        self.chanel = channel
        self.frequency = frequency
        self.dutycycle = 0
        global channel_config
        channel_config[channel] = Channel(channel,PWM,)
        board = getBoard()
        logger.info("Initialized PWM for Channel : {} at frequency : {}".format(channel,frequency))
    
    # where dc is the duty cycle (0.0 <= dc <= 100.0)
    def start(self, dutycycle):
        """
        Start software PWM
        dutycycle - the duty cycle (0.0 to 100.0)
        """
        self.dutycycle = dutycycle
        board = getBoard()
        logger.info("start pwm on channel : {} with Duty cycle : {}".format(self.chanel,dutycycle))
    
    # where freq is the new frequency in Hz
    def ChangeFrequency(self, frequency):
        """
        Change the frequency
        frequency - frequency in Hz (freq > 1.0)
        """
        board = getBoard()
        logger.info("Freqency Changed for channel : {} from : {} -> to : {}".format(self.chanel,self.frequency,frequency))
        self.frequency = frequency

    # where 0.0 <= dc <= 100.0
    def ChangeDutyCycle(self, dutycycle):
        """
        Change the duty cycle
        dutycycle - between 0.0 and 100.0
        """
        board = getBoard()
        self.dutycycle = dutycycle
        logger.info("Dutycycle Changed for channel : {} from : {} -> to : {}".format(self.chanel,self.dutycycle,dutycycle))
    
    # stop PWM generation
    def stop(self):
        board = getBoard()
        logger.info("Stop pwm on channel : {} with Duty cycle : {}".format(self.chanel,self.dutycycle))


def cleanup(channel=None):
    """
    Clean up by resetting all GPIO channels that have been used by this program to INPUT with no pullup/pulldown and no event detection
    [channel] - individual channel or list/tuple of channels to clean up.  Default - clean every channel that has been used.
    """
    board = getBoard()
    if channel is not None:
        logger.info("Cleaning Up Channel : {}".format(channel))
        setup_gpio(channel, INPUT, PUD_OFF)
        board.gpio_direction[channel] = -1
        board.channelConfigs[channel] = None
        board.channelEvents[channel] = None

        found = 1
    else:
        logger.info("Cleaning Up all channels")
        board.channelConfigs[channel] = {}
        board.channelEvents = {}
        
        i = 0 
        while i < 54:
            if not board.gpio_direction[i] == -1:
                setup_gpio(i, INPUT, PUD_OFF)
                board.gpio_direction[i] = -1
                found = 1
            i += 1
    board.cleanUp()
  
        
def getBoard():
    rpib = PiBoard.Board.getInstance()
    if rpib == None:
        rpib = PiBoard.Board()
    return rpib


def get_gpio_number(_channel, _gpio):
    '''
    Will only work with BCM
    
    '''
    return "0" + ":" + str(_channel)


def setup_gpio(chanel,direction,pud):
    print(chanel)
    print(direction)
    print(pud)
