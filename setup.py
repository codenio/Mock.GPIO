import setuptools

from distutils.util import convert_path

with open('DESCRIPTION.md', 'r') as readme:
  long_description = readme.read()

with open('requirements.txt', 'r') as requirements_file:
  requirements_text = requirements_file.read()

requirements = requirements_text.split()

pkg_ns = {}

ver_path = convert_path('Mock/__init__.py')
with open(ver_path) as ver_file:
    exec(ver_file.read(), pkg_ns)

setuptools.setup(
      name='Mock.GPIO',
      version=pkg_ns['__version__'],
      description='Mock Library for RPi.GPIO',
      url='https://github.com/codenio/',
      author='Aananth K',
      author_email='aananthraj1995@gmail.com',
      license='GPL-3.0',
      packages=setuptools.find_packages(),
      zip_safe=False,
      long_description_content_type="text/markdown",
      long_description=long_description,
      install_requires=requirements
)