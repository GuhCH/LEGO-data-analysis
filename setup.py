from setuptools import setup
from setuptools import find_packages

setup(
    name='LEGOSetAnalysis',
    version='0.0.1', 
    description='',
    url='https://github.com/GuhCH/LEGO-data-analysis',
    author='Joe Gocher',
    license='MIT',
    packages=find_packages(),
    install_requires=['datetime','pandas','pyspark','setuptools','multiprocessing'],
)