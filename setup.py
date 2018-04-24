#!/usr/bin/env python

from setuptools import (setup, find_packages)


description = 'API for real-time video rendering'
setup(
    name='vydemo',
    description=description,
    packages=find_packages(),
    package_data={
        'vydemo.app': ['data/*.mp4'],
    },
    entry_points={
        'console_scripts': [
            'vydemo-let-the-sun-shine = vydemo.app:let_the_sun_shine',
        ],
    }
)
