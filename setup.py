#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

requirements = [ ]

test_requirements = [ ]

setup(
    author="Avadhani Jonnavithula",
    author_email='',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Python package to help demonstrate testing and mocking",
    install_requires=requirements,
    license="MIT license",
    include_package_data=True,
    keywords='testlib',
    name='testlib',
    packages=find_packages(include=['testlib', 'testlib.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/avadhanij6si/py-testing-examples',
    version='0.1.0',
    zip_safe=False,
)
