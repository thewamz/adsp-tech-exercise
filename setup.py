#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Setup script for python build system
"""
from setuptools import find_packages, setup

setup(
    name="adsp",
    use_scm_version=True,
    setup_requires=["setuptools_scm"],
    packages=find_packages(exclude=("tests",)),
    package_data={"": ["*.json"]},
    include_package_data=True,
    description=(
        "Retrieve stop and search data from the Metropolitan Police Service API"
    ),
    author="Tinashe Wamambo",
    author_email="tinashe.wamambo@hotmail.co.uk",
    url="https://github.com/thewamz/adsp-tech-exercise",
    python_requires=">=3.10",
    install_requires=(
        "requests",
        "pandas",
        "importlib_metadata",
        "importlib_resources",
    ),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Operating System :: Linux",
        "Programming Language :: Python :: 3.10",
    ],
    entry_points={"console_scripts": ("adsp=adsp.entry:main")},
)
