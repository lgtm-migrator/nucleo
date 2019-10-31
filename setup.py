#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

requirements = [ ]

setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest', ]

setup(
    author="Ronak Shah",
    author_email='rons.shah@gmail.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    description="Workflow that creates all the bam files for the MSK-ACCESS fastq file",
    install_requires=requirements,
    license="Apache Software License 2.0",
    long_description=readme + '\n\n' + "Workflow that creates all the bam files for the MSK-ACCESS fastq file",
    include_package_data=True,
    keywords='fastq_to_bam',
    name='fastq_to_bam',
    packages=find_packages(include=['fastq_to_bam']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/rhshah/fastq_to_bam',
    version='0.1.1',
    zip_safe=False,
)
