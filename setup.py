# !/usr/bin/python
# -*- coding: utf-8 -*-
#
################################################################################
#
#   Copyright 2017-2018 Félix Brezo and Yaiza Rubio
#       (i3visio, contacto@i3visio.com)
#
#   This file is part of osrframework_server. You can redistribute it and/or
#   modify it under the terms of the GNU Affero General Public License as
#   published by the Free Software Foundation, either version 3 of the License,
#   or (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful, but WITHOUT
#   ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
#   FITNESS FOR A PARTICULAR PURPOSE. See the GNU Affero General Public License
#   for more details.
#
#   You should have received a copy of the GNU Affero General Public License
#   along with this program. If not, see <http://www.gnu.org/licenses/>.
#
################################################################################

import os
import sys
from setuptools import setup, find_packages

import osrframework.utils.configuration as configuration

import osrframework_console


print("[*] Launching the installation of the osrframework_console module...")
# Launching the setup
setup(
    name="osrframework_console",
    version=osrframework_console.__version__,
    description="OSRFramework Console - A terminal-based user interface to interact with OSRFramework utils.",
    author="Felix Brezo and Yaiza Rubio",
    author_email="contacto@i3visio.com",
    url="http://github.com/i3visio/osrframework_console",
    license="COPYING",
    keywords = "python osint harvesting profiling username socialmedia forums",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
        'Programming Language :: Python :: 2.7',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Telecommunications Industry',
        'Topic :: Communications',
        'Topic :: Internet :: WWW/HTTP :: Indexing/Search',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Scientific/Engineering :: Visualization',
        'Topic :: Text Processing :: Markup :: HTML'
    ],
    packages = find_packages(),
    entry_points={
        'console_scripts': [
            "osrframework_console = osrframework_console.console:main",
            "osrfconsole = osrframework_console.console:main",
        ],
    },
    install_requires=[
        "osrframework>=0.18.0"
    ]
)
