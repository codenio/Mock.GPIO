# Mock.GPIO

[![CI](https://github.com/codenio/Mock.GPIO/actions/workflows/ci.yml/badge.svg)](https://github.com/codenio/Mock.GPIO/actions/workflows/ci.yml)

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

Minimal `Makefile` targets:

```bash
make help          # list targets
make install       # local install via scripts/install.sh
make test          # run pytest
make clean         # remove build artifacts
make build         # build sdist and wheel
make publish-test  # upload to Test PyPI
make publish       # upload to PyPI
```

### Test across Python versions (tox + pyenv)

```bash
# install interpreters
pyenv install 3.10.14 3.11.9 3.12.6 3.13.0 pypy3.11-7.3.17
eval "$(pyenv init -)"
pyenv local 3.10.14 3.11.9 3.12.6 3.13.0 pypy3.11-7.3.17

# run tox matrix
make tox
```

Note: Runtime `dependencies` are intentionally empty to avoid issues on PyPy (e.g., `nh3`/PyO3). Dev and packaging tools are installed separately.

## Contributing

Contributions are welcome! Please open an issue or submit a PR.

## Thanks to contributors

Thanks to all the amazing contributors who make this project better. See the full list on the
[Contributors page](https://github.com/codenio/Mock.GPIO/graphs/contributors).

## License

Licensed under GPL-3.0. See `LICENSE`.
