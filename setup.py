#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('requirements.txt') as fd:
    requirements = [dependency.strip() for dependency in fd if dependency.strip()]

with open('version') as fd:
    version = fd.read().strip()

setup_args = {
    'name': 'payment_paygate_service',
    'version': version,
    'description': "gRPC test service",
    'long_description': "Update this!",
    'author': "Bongani Sibanda",
    'author_email': 'sibandabongz@gmail.com',
    'url': 'https://github.com/...',
    'packages': find_packages(),
    'package_dir': {'test_service':
                    'test_service'},
    'package_data': {
        'test_service': []
     },
    'install_requires': requirements,
    'keywords': 'grpc',
    'classifiers': [
        'Development Status :: 2 - Pre-Alpha',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
    ],
    'entry_points': {
        'console_scripts': [
            'test_service=test_service.service:serve',
        ],
    }
}

setup(**setup_args)
