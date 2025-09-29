# LOG_LEVEL=Info PYTHONPATH=. uv run pytest

"""
Pytest tests for Mock.GPIO module.
* GPIO: General Purpose Input/Output
* PWM:Pulse Width Modulation

TODO: Add tests for:
* GPIO.wait_for_edge()
* GPIO.add_event_detect()
* GPIO.event_detected()
* GPIO.add_event_callback()
* GPIO.remove_event_detect()
* GPIO.gpio_function()
"""

import pytest

try:
    import RPi.GPIO as GPIO
except ImportError:
    import Mock.GPIO as GPIO


def test_gpio_start_stop(caplog):
    with pytest.raises(
        AttributeError, match="module 'Mock.GPIO' has no attribute 'start'"
    ):
        GPIO.start()
    with pytest.raises(
        AttributeError, match="module 'Mock.GPIO' has no attribute 'stop'"
    ):
        GPIO.stop()


def test_gpio_getmode_setmode(caplog):
    assert GPIO.getmode() == 0
    assert caplog.record_tuples == []  # No log messages should be generated
    assert GPIO.BCM == 11
    assert GPIO.setmode(GPIO.BCM) is None
    assert caplog.record_tuples == []  # No log messages should be generated
    assert GPIO.getmode() == GPIO.BCM  # Should return BCM value (11) after setting mode
    assert caplog.record_tuples == []  # No log messages should be generated


def test_gpio_setwarnings(caplog):
    assert GPIO.setwarnings(False) is None
    assert "Set warnings as False" in caplog.record_tuples[-1]


def test_gpio_setup(caplog):
    assert GPIO.setup(15, GPIO.OUT) is None
    assert (
        "Setup channel : 15 as 0 with initial :0 and pull_up_down 20"
        in caplog.record_tuples[-1]
    )


def test_gpio_output_input(caplog):
    """
    Sending a list or tuple of channels to GPIO.output() works, but sensing a single
    channel integer fails which seems to be a bug.
    """
    channel = 7
    GPIO.setup(channel, GPIO.OUT)
    # 'channel' is a list works as expected.
    assert GPIO.output([channel], GPIO.HIGH) is None
    assert "Output channel : 7 with value : 1" in caplog.record_tuples[-1]
    # 'channel' is a tuple works as expected.
    assert GPIO.output((channel,), GPIO.LOW) is None
    assert "Output channel : 7 with value : 0" in caplog.record_tuples[-1]

    # 'channel' as a single integer now works correctly (bug was fixed)
    assert GPIO.output(channel, GPIO.HIGH) is None
    assert "Output channel : 7 with value : 1" in caplog.record_tuples[-1]

    assert GPIO.input(channel) is None
    assert "Reading from channel 7" in caplog.record_tuples[-1]


def test_gpio_change_frequency(caplog):
    with pytest.raises(
        AttributeError,
        match="module 'Mock.GPIO' has no attribute 'ChangeFrequency'",
    ):
        GPIO.ChangeFrequency(50)


def test_gpio_change_duty_cycle(caplog):
    with pytest.raises(
        AttributeError, match="module 'Mock.GPIO' has no attribute 'ChangeDutyCycle'"
    ):
        GPIO.ChangeDutyCycle(50)


def test_gpio_cleanup(caplog):
    assert GPIO.cleanup() is None
    assert "Cleaning up all channels" in caplog.record_tuples[-1]


def test_gpio_channel_in(caplog):
    channel_in = GPIO.Channel(2, GPIO.IN)
    assert caplog.record_tuples == []  # No log messages should be generated
    assert channel_in.channel == 2
    assert channel_in.direction == GPIO.IN
    assert GPIO.input(2) is None
    assert "Reading from channel 2" in caplog.record_tuples[-1]


def test_gpio_channel_out(caplog):
    channel_out = GPIO.Channel(3, GPIO.OUT)
    assert caplog.record_tuples == []  # No log messages should be generated
    assert channel_out.channel == 3
    assert channel_out.direction == GPIO.OUT
    assert GPIO.output([3], True) is None
    assert "Output channel : 3 with value : True" in caplog.record_tuples[-1]
    assert GPIO.output((3,), False) is None
    assert "Output channel : 3 with value : False" in caplog.record_tuples[-1]
    # Single integer call now works correctly (bug was fixed)
    assert GPIO.output(3, False) is None
    assert "Output channel : 3 with value : False" in caplog.record_tuples[-1]


def test_gpio_pulse_width_modulation(caplog):
    pwm = GPIO.PWM(4, 50)  # channel 4 at 50Hz
    assert (
        "Initialized PWM for channel : 4 at frequency : 50" in caplog.record_tuples[-1]
    )
    assert pwm.channel == 4
    assert pwm.frequency == 50
    assert pwm.start(75) is None
    assert "Start pwm on channel : 4 with duty cycle : 75" in caplog.record_tuples[-1]
    assert pwm.ChangeDutyCycle(25) is None
    assert (
        "Dutycycle changed for channel : 4 from : 25 -> to : 25"
        in caplog.record_tuples[-1]
    )
    assert pwm.ChangeFrequency(100) is None
    assert (
        "Frequency changed for channel : 4 from : 50 -> to : 100"
        in caplog.record_tuples[-1]
    )
    assert pwm.stop() is None
    assert "Stop PWM on channel : 4 with duty cycle : 25" in caplog.record_tuples[-1]
