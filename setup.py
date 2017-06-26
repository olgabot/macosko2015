#!/usr/bin/env python

from setuptools import setup

version = '1.0.0'

required = open('requirements.txt').read().split('\n')

setup(
    name='macosko2015',
    version=version,
    description='Expression data for Macosko et al, "Highly Parallel Genome-wide Expression Profiling of Individual Cells Using Nanoliter Droplets," Cell (2015)',
    author='Olga Botvinnik',
    author_email='olga.botvinnik@gmail.com',
    url='https://github.com/olgabot/macosko2015',
    packages=['macosko2015'],
    install_requires=required,
    long_description='See ' + 'https://github.com/olgabot/macosko2015',
    license='MIT'
)
