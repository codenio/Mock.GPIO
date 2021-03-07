from setuptools import setup, find_packages

from distutils.util import convert_path

long_description ="""
# GPIOEmulator

The easiest way to use this package is to install using pip3 for python 3

```bash
$ sudo pip3 install Mock.GPIO
```

To use the emulator just type the following at the beginning of your script.

```python
from Mock.GPIO import GPIO
```

## Works with

- [python 3.6.8](https://www.python.org/downloads/release/3.6.8)

## Simulation

This library simulates the following functions which are used in the RPi.GPIO library.

- GPIO.setmode()
- GPIO.getmode()
- GPIO.setwarnings()
- GPIO.setup()
- GPIO.output()
- GPIO.input()
- GPIO.wait_for_edge()
- GPIO.add_event_detect()
- GPIO.event_detected()
- GPIO.add_event_callback()
- GPIO.remove_event_detect()
- GPIO.gpio_function()
- GPIO.start()
- GPIO.ChangeFrequency()
- GPIO.ChangeDutyCycle()
- GPIO.stop()
- GPIO.cleanup()
"""

pkg_ns = {}

ver_path = convert_path('Mock/__init__.py')
with open(ver_path) as ver_file:
    exec(ver_file.read(), pkg_ns)

setup(
      name='Mock.GPIO',
      version=pkg_ns['__version__'],
      description='Mock Library for RPi.GPIO',
      url='https://github.com/codenio/',
      author='Aananth K',
      author_email='aananthraj1995@gmail.com',
      license='GPL-3.0',
      packages=find_packages(exclude=[]),
      install_requires=[],
      zip_safe=False,
      long_description_content_type="text/markdown",
      long_description=long_description,
)
