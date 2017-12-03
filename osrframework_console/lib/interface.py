# -*- coding: utf-8 -*-
#
################################################################################
#
#   Copyright 2017 Félix Brezo and Yaiza Rubio
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

import argparse
import cmd as cmd
import json
import os
import sys

import osrframework
import osrframework.utils.configuration as configuration
import osrframework.utils.banner as banner
import osrframework.utils.general as general
import osrframework.utils.platform_selection as platform_selection
import osrframework.utils.regexp_selection as regexp_selection
import osrframework.domainfy as domainfy
import osrframework.entify as entify
import osrframework.mailfy as mailfy
import osrframework.phonefy as phonefy
import osrframework.searchfy as searchfy
import osrframework.usufy as usufy

import osrframework_console.lib.utils as utils


UTILS = [
    "domainfy",
    "entify", #: regexp_selection.getAllRegexpNames(),
    "mailfy", # mailfy.EMAIL_DOMAINS,
    "phonefy",
    "searchfy",
    "usufy", # platform_selection.getAllPlatformNames("usufy"),
]

################################################################################
# Defining the abstract class of the utils that will be managed                #
################################################################################


class OSRFConsoleUtil(cmd.Cmd):
    """
    Simple class from which of a msfconsole-like interactive interface
    """
    # Setting up the name of the module
    UNAME = "Abstract Util"

    intro = ""
    # Defining the prompt
    prompt = general.emphasis('\n (' + UNAME + ') > ')
    # Defining the character to create hyphens
    ruler = '-'

    # Defining the configuration for this module
    CONFIG = {}
    CONFIG["OPTION"] = {
        "DESCRIPTION" : "An example of option.",
        "CURRENT_VALUE" : "Hello",
        "DEFAULT_VALUE" : "Hello",
        "REQUIRED" : False,
        "OPTIONS" : ["world", "people"]
    }
    CONFIG["OUTPUT"] = {
        "DESCRIPTION" : "The path to the output folder where the files will be created.",
        "CURRENT_VALUE" : "./",
        "DEFAULT_VALUE" : "./",
        "REQUIRED" : False,
        "OPTIONS" : []
    }
    CONFIG["EXTENSION"] = {
        "DESCRIPTION" : "The default extension of the files to be written.",
        "CURRENT_VALUE" : "csv",
        "DEFAULT_VALUE" : "csv",
        "REQUIRED" : False,
        "OPTIONS" : ['csv', 'xls', 'xlsx', 'json', 'gml']
    }

    def _checkIfRequiredAreSet(self):
        """
        Internal function to check if the required parameters have been set
        """
        details = ""
        for key in self.CONFIG.keys():
            if self.CONFIG[key]["REQUIRED"] and self.CONFIG[key]["CURRENT_VALUE"] == None:
                return False
        return True

    def _getOptionsDescription(self):
        """
        Internal function to collect the description of each and every parameter

        Returns:
        --------
            string: a string containing the description of each option.
        """
        details = ""
        for key in self.CONFIG.keys():
            details += "\t- " + key + ". " + self.CONFIG[key]["DESCRIPTION"] + "\n"
        return details

    def _getParams(self):
        """
        Function that creates the array with the params of this function

        Returns:
        --------
            list: a list of the params that can be used
        """
        # Creating the parameters as if they were created using the command line
        params = ["-h"]
        return params

    def do_set(self, line):
        """
        Setting the variables defined in CONFIG

        You can check their values at any time by typing 'show options'.

        Args:
        -----
            line: the string of the line typed.
        """
        try:
            parameter, value = line.split(" ", 1)
            # Setting the parameter
            if parameter in self.CONFIG.keys():
                splittedValues = value.split(" ")

                # Verifying if the parameter is in the options
                if len(self.CONFIG[parameter]["OPTIONS"]) > 0:

                    for s in splittedValues:
                        if s not in self.CONFIG[parameter]["OPTIONS"]:
                            raise Exception("ERROR: the value '" + s + "' provided is not valid.")
                # Setting the value
                self.CONFIG[parameter]["CURRENT_VALUE"] = splittedValues
                print(general.success("\n[OK] " + parameter + "=" + str(value)))
            else:
                raise Exception("ERROR: parameter not valid.")
        except Exception as e:
            print(general.error("\n[!!] ERROR: Not enough parameters provided. Usage: set OPTION VALUE."))
            print(general.error(str(e)))

    def complete_set(self, text, line, begidx, endidx):
        # First, we will try to get the available parameters
        if len(line.split(" ")) == 2:
            if not text:
                completions = self.CONFIG.keys()
            else:
                completions = [ f
                    for f in self.CONFIG.keys()
                    if f.startswith(text.upper())
                ]
        # We are setting the value
        elif len(line.split(" ")) >= 3:
            # First, we get the given parameter
            parameter = line.split(" ")[1]
            if not text:
                completions = self.CONFIG[parameter]["OPTIONS"]
            else:
                completions = [ f
                    for f in self.CONFIG[parameter]["OPTIONS"]
                    if f.startswith(text.lower())
                ]
        return completions

    def do_unset(self, line):
        """
        Unsetting the variables defined in CONFIG

        You can check their values at any time by typing 'show options' and
        unsetting all the options at once by typing 'unset all'.

        Args:
        -----
            line: the string of the line typed.

        Raises:
        -------
            ValueError: if the parameter is not valid.
        """
        try:
            parameter = line.split(" ")[0]
            # Getting the parameter
            if parameter in self.CONFIG.keys():
                # Unsetting the value
                self.CONFIG[parameter]["CURRENT_VALUE"] = self.CONFIG[parameter]["DEFAULT_VALUE"]
                print(general.info(parameter + " reseted to '" + str(self.CONFIG[parameter]["DEFAULT_VALUE"]) + "'."))
            elif parameter == "all":
                for p in self.CONFIG.keys():
                    # Unsetting all the values
                    self.CONFIG[p]["CURRENT_VALUE"] = self.CONFIG[p]["DEFAULT_VALUE"]
                print(general.success("\nAll parameters reseted to their default values."))
            else:
                raise ValueError("ERROR: parameter not valid.")
        except Exception as e:
            print(general.error("\n[!!] ERROR: Not enough parameters provided. Usage: unset OPTION"))
            print(general.error("Traceback: " + str(e)))

    def complete_unset(self, text, line, begidx, endidx):
        # First, we will try to get the available parameters
        unsettingOptions = ["all"] + self.CONFIG.keys()

        if len(line.split(" ")) == 2:
            if not text:
                completions = unsettingOptions
            else:
                completions = [ f
                    for f in unsettingOptions
                    if f.startswith(text.upper())
                ]
        return completions

    def do_run(self, line):
        """
        Command that send the order to the framework to launch this util

        Args:
        -----
            line: the string of the line typed.
        """
        if self._checkIfRequiredAreSet():
            print(general.info("\nLaunching the util...\n"))
        else:
            print(general.error("\n[!!] ERROR: There are required parameters which have not been set."))
            self.do_show("options")

    def do_show(self, line):
        """
        Showing the information about the module

        The things to show are: 'options' and 'command'.
            - 'options' will show the current values of each and every
                parameter.
            - 'command' will show the command needed to launch the module as is
                using the cli applications.

        Args:
        -----
            line: the string of the line typed.
        """
        if line.lower() == "options":
            print(general.emphasis("\n\tOptions\n\t-------\n"))
            for key in self.CONFIG.keys():
                print("\t- " + (key + (" (*)." if self.CONFIG[key]["REQUIRED"] else ".") ).ljust(14) + "" + self.CONFIG[key]["DESCRIPTION"])

            print(general.emphasis("\n\tCurrent values\n\t-------------\n"))
            for key in self.CONFIG.keys():
                print("\t- " + (key + (" (*)" if self.CONFIG[key]["REQUIRED"] else "") + ": ").ljust(14) + general.info("" if self.CONFIG[key]["CURRENT_VALUE"] == None else utils.listToString(self.CONFIG[key]["CURRENT_VALUE"])))

        elif line.lower() == "command":
            print(general.emphasis("\n\tTerminal command\n\t----------------\n\t\t") + "$ "+ general.info(self.createCommandLine()))

    def complete_show(self, text, line, begidx, endidx):
        # First, we will try to get the available parameters
        showOptions = ["options", "command"]

        if len(line.split(" ")) == 2:
            if not text:
                completions = showOptions
            else:
                completions = [ f
                    for f in showOptions
                    if f.startswith(text.lower())
                ]
        return completions

    def createCommandLine(self):
        """
        Method to build the command line command

        This method will build the command to run the same actions defined in
        using this tool.

        Returns:
        --------
            String: the string to type in the terminal
        """
        if self._checkIfRequiredAreSet():
            command = self.UNAME
            # Getting the params
            params = self._getParams()
            for p in params:
                command += " " +p
            # Returning the command
            return command
        else:
            return self.UNAME + " -h" + general.warning(" # Option '-h' shown since not all the required parameters are set. ")

    def do_info(self, line):
        """
        Shows all the information available about the module.

        Args:
        -----
            line: the string of the line typed.
        """
        print(self.description)
        self.do_show("options")
        self.do_show("command")

    def do_back(self, line):
        """
        Command to unload the current util and goes back to the main console

        Args:
        -----
            line: the string of the line typed.
        """
        return True

    def do_exit(self, line):
        """
        This command will exit the osrfconsole normally

        Args:
        -----
            line: the string of the line typed.
        """
        print(general.info("\nExiting the program...\n"))
        sys.exit()
