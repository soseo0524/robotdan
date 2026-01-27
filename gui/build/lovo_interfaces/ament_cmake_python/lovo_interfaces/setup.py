from setuptools import find_packages
from setuptools import setup

setup(
    name='lovo_interfaces',
    version='0.0.0',
    packages=find_packages(
        include=('lovo_interfaces', 'lovo_interfaces.*')),
)
