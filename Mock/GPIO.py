"""
Mock Library for RPi.GPIO
"""

import time
import logging
import os

logger = logging.getLogger(__name__)

log_level = os.getenv('LOG_LEVEL')

if log_level is not None:
    if log_level.lower() == "info":
        logger.setLevel(logging.INFO)
    if log_level.lower() == "debug":
        logger.setLevel(logging.DEBUG)
    if log_level.lower() == "warning":
        logger.setLevel(logging.WARNING)
    if log_level.lower() == "error":
        logger.setLevel(logging.ERROR)
    if log_level.lower() == "critical":
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

_mode = 0

channel_config = {}

#flags
setModeDone = False

class Channel:
    def __init__(self,channel, direction, initial=0,pull_up_down=PUD_OFF):
        self.channel = channel
        self.direction = direction
        self.initial = initial
        self.pull_up_down = pull_up_down


#GPIO LIBRARY Functions
def setmode(mode):
    """
    Set up numbering mode to use for channels.
    BOARD - Use Raspberry Pi board numbers
    BCM   - Use Broadcom GPIO 00..nn numbers
    """
    # GPIO = GPIO()
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
    return _mode

def setwarnings(flag):
    """
    Enable or disable warning messages
    """
    logger.info("Set warnings as {}".format(flag))

def setup(channels, direction, initial=0,pull_up_down=PUD_OFF):
    """
    Set up a GPIO channel or list of channels with a direction and (optional) pull up/down control
    channels        - either board pin number or BCM number depending on which mode is set.
    direction      - IN or OUT
    [pull_up_down] - PUD_OFF (default), PUD_UP or PUD_DOWN
    [initial]      - Initial value for an output channel

    """
    global channel_config

    if type(channels) is list or type(channels) is tuple:
        for channel in channels:
            logger.info("Setup channel : {} as {} with initial :{} and pull_up_down {}".format(channel,direction,initial,pull_up_down))
            channel_config[channel] = Channel(channel, direction, initial, pull_up_down)
    else:
        logger.info("Setup channel : {} as {} with initial :{} and pull_up_down {}".format(channels,direction,initial,pull_up_down))
        channel_config[channels] = Channel(channels, direction, initial, pull_up_down)

def output(channels, values):
    """
    Output to a GPIO channel or list of channels
    channels - either board pin number or BCM number depending on which mode is set.
    values   - 0/1 or False/True or LOW/HIGH

    """
    if type(channels) is list or type(channels) is tuple:
        for channel in channels:
            if type(values) is list or type(values) is tuple:
                for value in values:
                    logger.info("Output channel : {} with value : {}".format(channel, value))
            else:
                logger.info("Output channel : {} with value : {}".format(channel, values))
    else:
        if type(values) is list or type(values) is tuple:
            for value in values:
                logger.info("Output channel : {} with value : {}".format(channel, value))
        else:
            logger.info("Output channel : {} with value : {}".format(channel, values))
        

def input(channel):
    """
    Input from a GPIO channel.  Returns HIGH=1=True or LOW=0=False
    channel - either board pin number or BCM number depending on which mode is set.
    """
    logger.info("Reading from channel {}".format(channel))

def wait_for_edge(channel,edge,bouncetime,timeout):
    """
    Wait for an edge.  Returns the channel number or None on timeout.
    channel      - either board pin number or BCM number depending on which mode is set.
    edge         - RISING, FALLING or BOTH
    [bouncetime] - time allowed between calls to allow for switchbounce
    [timeout]    - timeout in ms
    """
    logger.info("Waiting for edge : {} on channel : {} with bounce time : {} and Timeout :{}".format(edge,channel,bouncetime,timeout))


def add_event_detect(channel,edge,callback=None,bouncetime=None):
    """
    Enable edge detection events for a particular GPIO channel.
    channel      - either board pin number or BCM number depending on which mode is set.
    edge         - RISING, FALLING or BOTH
    [callback]   - A callback function for the event (optional)
    [bouncetime] - Switch bounce timeout in ms for callback
    """
    logger.info("Event detect added for edge : {} on channel : {} with bounce time : {} and callback {}".format(edge,channel,bouncetime,callback))

def event_detected(channel):
    """
    Returns True if an edge has occurred on a given GPIO.  You need to enable edge detection using add_event_detect() first.
    channel - either board pin number or BCM number depending on which mode is set.
    """
    logger.info("Waiting for even detection on channel :{}".format(channel))

def add_event_callback(channel,callback):
    """
    Add a callback for an event already defined using add_event_detect()
    channel      - either board pin number or BCM number depending on which mode is set.
    callback     - a callback function
    """
    logger.info("Event callback : {} added for channel : {}".format(callback,channel))

def remove_event_detect(channel):
    """
    Remove edge detection for a particular GPIO channel
    channel - either board pin number or BCM number depending on which mode is set.
    """
    logger.info("Event detect removed for channel : {}".format(channel))

def gpio_function(channel):
    """
    Return the current GPIO function (IN, OUT, PWM, SERIAL, I2C, SPI)
    channel - either board pin number or BCM number depending on which mode is set.
    """
    logger.info("GPIO function of channel : {} is {}".format(channel,channel_config[channel].direction))


class PWM:
    # initialise PWM channel
    def __init__(self, channel, frequency):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        self.channel = channel
        self.frequency = frequency
        self.dutycycle = 0
        global channel_config
        channel_config[channel] = Channel(channel,PWM,)
        logger.info("Initialized PWM for channel : {} at frequency : {}".format(channel,frequency))

    # where dc is the duty cycle (0.0 <= dc <= 100.0)
    def start(self, dutycycle):
        """
        Start software PWM
        dutycycle - the duty cycle (0.0 to 100.0)
        """
        self.dutycycle = dutycycle
        logger.info("Start pwm on channel : {} with duty cycle : {}".format(self.channel,dutycycle))

    # where freq is the new frequency in Hz
    def ChangeFrequency(self, frequency):
        """
        Change the frequency
        frequency - frequency in Hz (freq > 1.0)
        """
        logger.info("Freqency changed for channel : {} from : {} -> to : {}".format(self.channel,self.frequency,frequency))
        self.frequency = frequency

    # where 0.0 <= dc <= 100.0
    def ChangeDutyCycle(self, dutycycle):
        """
        Change the duty cycle
        dutycycle - between 0.0 and 100.0
        """
        self.dutycycle = dutycycle
        logger.info("Dutycycle changed for channel : {} from : {} -> to : {}".format(self.channel,self.dutycycle,dutycycle))

    # stop PWM generation
    def stop(self):
        logger.info("Stop PWM on channel : {} with duty cycle : {}".format(self.channel,self.dutycycle))


def cleanup(channels=None):
    """
    Clean up by resetting all GPIO channels that have been used by this program to INPUT with no pullup/pulldown and no event detection
    [channels] - individual channel or list/tuple of channels to clean up.  Default - clean every channel that has been used.
    """
    if channels is not None:
        if type(channels) is list or type(channels) is tuple:
            for channel in channels:
                logger.info("Cleaning up channel : {}".format(channel))
        else:
            logger.info("Cleaning up channel : {}".format(channels))
    else:
        logger.info("Cleaning up all channels")
