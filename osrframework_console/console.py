#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
################################################################################
#
#   Copyright 2017-2018 Félix Brezo and Yaiza Rubio
#       (i3visio, contacto@i3visio.com)
#
#   This file is part of osrframework_console. You can redistribute it and/or
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


import cmd as cmd
import os
import sys

import osrframework
import osrframework.utils.configuration as configuration
import osrframework.utils.banner as banner
import osrframework.utils.general as general
import osrframework.utils.platform_selection as platform_selection
import osrframework.utils.regexp_selection as regexp_selection
import osrframework.domainfy as domainfy
import osrframework.mailfy as mailfy

import osrframework_console.lib.utils as utils
from osrframework_console.lib.interface import OSRFConsoleUtil
from osrframework_console.apps.domainfy import OSRFConsoleDomainfy
from osrframework_console.apps.entify import OSRFConsoleEntify
from osrframework_console.apps.mailfy import OSRFConsoleMailfy
from osrframework_console.apps.phonefy import OSRFConsolePhonefy
from osrframework_console.apps.searchfy import OSRFConsoleSearchfy
from osrframework_console.apps.usufy import OSRFConsoleUsufy

UTILS = [
    "domainfy",
    "entify", #: regexp_selection.getAllRegexpNames(),
    "mailfy", # mailfy.EMAIL_DOMAINS,
    "phonefy",
    "searchfy",
    "usufy", # platform_selection.getAllPlatformNames("usufy"),
]


class OSRFConsoleMain(cmd.Cmd):
    """
    OSRFramework console application to control the different framework utils

    The user can type 'help' at any time to find the available commands included
    in the framework.
    """

    DISCLAIMER = """\tOSRFramework """ + osrframework.__version__ + """ - Copyright (C) F. Brezo and Y. Rubio (i3visio) 2016-2017

    This program comes with ABSOLUTELY NO WARRANTY. This software is free
    software, and you are really welcome to redistribute it under certain
    conditions. For additional information about the terms and conditions of the
    AGPLv3+ license, visit <http://www.gnu.org/licenses/agpl-3.0.txt>."""

    intro = banner.text + "\n" + DISCLAIMER + "\n"

    info  = general.info("") + general.emphasis("""
    General information
    ===================""") + """

    OSRFConsole is a terminal GUI to interact with OSRFramework utilities.
    OSRFramework stands for Open Sources Research Framework. It includes a set
    of tools that help the analyst in the task of user profiling making use of
    different OSINT tools.

    To get additional information about the available commands type 'help'.

    """ + general.emphasis("""Modules available:
    ------------------""") + """

        - """ + general.success("usufy") + """ --> the Jewel of the Chrown. A tool that verifies if a
            username exists in """ + str(len(platform_selection.getAllPlatformNames("usufy")))  + """ platforms.
        - """ + general.success("mailfy") + """ --> a tool to check if a username has been registered in up to
            """ + str(len(mailfy.EMAIL_DOMAINS )) + """ email providers.
        - """ + general.success("searchfy") + """ --> a tool to look for profiles using full names and other
            info in """ + str(len(platform_selection.getAllPlatformNames("searchfy")))  + """ platforms.
        - """ + general.success("domainfy") + """ --> a tool to check the existence of a given domain in up to
            """ + str(domainfy.getNumberTLD()) + """ different TLDs.
        - """ + general.success("phonefy") + """ --> a tool that checks if a phone number has been linked to
            spam practices in """ + str(len(platform_selection.getAllPlatformNames("phonefy")))  + """ platforms.
        - """ + general.success("entify") + """ --> a util to look for regular expressions using """ + str(len(regexp_selection.getAllRegexpNames())) + """ patterns."""

    # Appending the self.info data to the headers...
    intro += info

    # Defining the prompt
    prompt = general.emphasis('\nosrf > ')

    ruler = '='

    def do_info(self, line):
        """
        Command that shows again the general information about the application

        Args:
        -----
            line: the string of the line typed.
        """
        configInfo =  """

    """ + general.emphasis("""Additional configuration files:
    -------------------------------""") + """

    You will be able to find more configuration options in the following files
    in your system. The relevant paths are the ones that follow:"""
        # Get the configuration folders in each system
        paths = configuration.getConfigPath()

        configInfo += """

        - Configuration details about the login credentials in OSRFramework:
            """  + general.info(os.path.join(paths["appPath"], "accounts.cfg")) + """
        - Configuration details about the API credentials already configured:
            """  + general.info(os.path.join(paths["appPath"], "api_keys.cfg")) + """
        - Connection configuration about how the browsers will be connected:
            """  + general.info(os.path.join(paths["appPath"], "browser.cfg")) + """
        - General default configuration of the the utils:
            """  + general.info(os.path.join(paths["appPath"], "general.cfg")) + """
        - Directory containing default files as a backup:
            """  + general.info(paths["appPathDefaults"]) + """
        - Directory containing the user-defined patterns for entify.py:
            """  + general.info(paths["appPathPatterns"]) + """
        - Directory containing the user-defined wrappers for usufy platforms:
            """  + general.info(paths["appPathWrappers"])
        print(self.info + configInfo)

    def do_use(self, line):
        """
        This command will define which of the framework's utilities will be loaded.

        The available options are the following:
            - domainfy
            - entify
            - mailfy
            - phonefy
            - searchfy
            - usufy
        For example, type 'use usufy' to load the usufy util. You can always use
        the <TAB> to be helped using the autocomplete options.

        Args:
        -----
            line: the string of the line typed.
        """
        if line not in UTILS:
            print(general.warning("[!] Util is not correct. Try 'help use' to check the available options."))
            return False
        elif line == "domainfy":
            OSRFConsoleDomainfy().cmdloop()
        elif line == "entify":
            OSRFConsoleEntify().cmdloop()
        elif line == "mailfy":
            OSRFConsoleMailfy().cmdloop()
        elif line == "phonefy":
            OSRFConsolePhonefy().cmdloop()
        elif line == "searchfy":
            OSRFConsoleSearchfy().cmdloop()
        elif line == "usufy":
            OSRFConsoleUsufy().cmdloop()
        else:
            print(general.warning("[!] Not implemented yet. Try 'help use' to check the available options."))

    def complete_use(self, text, line, begidx, endidx):
        if not text:
            completions = UTILS
        else:
            completions = [ f
                for f in UTILS
                if f.startswith(text.lower())
            ]
        return completions

    def do_exit(self, line):
        """
        This command will exit the osrfconsole normally

        Args:
        -----
            line: the string of the line typed.
        """
        print("\nExiting...\n")
        sys.exit()


def main(params=None):
    """
    Main function that starts the loop

    Args:
    -----
        params: Arguments received in the command line. Not used now.

    Returns:
    --------
        A list of i3visio entities.
    """
    OSRFConsoleMain().cmdloop()


if __name__ == '__main__':
    main(sys.argv)
