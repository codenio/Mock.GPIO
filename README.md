# Mock.GPIO

Mock Library for RPi.GPIO.

Mock.GPIO helps you develop and debug GPIO-dependent code outside a Raspberry Pi (e.g. on macOS/Linux) while keeping the same API as `RPi.GPIO`. It prints intended actions when running off-device and works as a drop-in replacement on-device without code changes.

### Installation

```bash
pip3 install Mock.GPIO
```

### Quick start

```python
try:
    import RPi.GPIO as GPIO
except Exception:
    import Mock.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(15, GPIO.OUT)
GPIO.output(15, GPIO.HIGH)
```

### Supported API surface

- GPIO.setmode(), GPIO.getmode(), GPIO.setwarnings(), GPIO.setup(), GPIO.output(), GPIO.input()
- GPIO.wait_for_edge(), GPIO.add_event_detect(), GPIO.event_detected(), GPIO.add_event_callback(), GPIO.remove_event_detect()
- GPIO.gpio_function(), GPIO.start(), GPIO.ChangeFrequency(), GPIO.ChangeDutyCycle(), GPIO.stop(), GPIO.cleanup()

### Supported versions

- Python: 3.8–3.12

## Documentation

- [Library Overview](https://htmlpreview.github.io/?https://github.com/codenio/Mock.GPIO/blob/master/docs/Mock.GPIO.html)
- [Examples](examples)

## Development

This repo includes a standard `Makefile`.

```bash
# one-time setup
make requirements

# run tests
make test

# install locally (editable)
make dev-install

# build & publish
make build
make publish-test
make publish
```

Alternatively, you can use the scripts under `scripts/` directly.

## Contributing

Contributions are welcome! Please open an issue or submit a PR.

## License

Licensed under GPL-3.0. See `LICENSE`.
