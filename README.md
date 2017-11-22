OSRFramework Console
====================

An extension of OSRFramework: Open Sources Research Framework

Copyright (C) 2014-2017  F. Brezo and Y. Rubio, i3visio

[![Version in PyPI](https://img.shields.io/pypi/v/osrframework_maltego.svg)]()
[![License](https://img.shields.io/badge/license-GNU%20General%20Public%20License%20Version%203%20or%20Later-blue.svg)]()

1 - Description
---------------

This package will fix the dependencies to make OSRFramework is a terminal-based
UI that will help users to interact with OSRFramework applications using
Metasploit-like commands.

This package will automatically build and prepare the tools needed to make this
possible. For more information about OSRFramework check the main project:
<https://github.com/i3visio/osrframework>

2 - License: GNU GPLv3+
-----------------------

This is free software, and you are welcome to redistribute it under certain
conditions.

	This program is free software: you can redistribute it and/or modify
	it under the terms of the GNU General Public License as published by
	the Free Software Foundation, either version 3 of the License, or
	(at your option) any later version.

	This program is distributed in the hope that it will be useful,
	but WITHOUT ANY WARRANTY; without even the implied warranty of
	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
	GNU General Public License for more details.

	You should have received a copy of the GNU  General Public License
	along with this program. If not, see <http://www.gnu.org/licenses/>.


For more details on this issue, check the [COPYING](COPYING) file.

3 - Installation
----------------

Fast way to do it on any system for a user with administration privileges:
```
pip install osrframework_console
```
You can upgrade to the latest release of the framework with:
```
pip install osrframework_console --upgrade
```
This will manage the dependencies linked to OSRFramework for you and install the
latest version of the server version.


4 - Basic configuration
-----------------------

To start the application, just use:
```
osrfconsole
```
At any moment, the user can type `help` to check the avilable commands:
```
osrf > help

Documented commands (type help <topic>):
========================================
exit  help  info  use

osrf > use usufy

osrf (usufy) > info
```

5 - HACKING
-----------

If you want to extend add new transforms and you do not know where to start
from, check the [HACKING.md](doc/HACKING.md) file.

6 - AUTHORS
-----------

More details about the authors in the [AUTHORS.md](AUTHORS.md) file.
