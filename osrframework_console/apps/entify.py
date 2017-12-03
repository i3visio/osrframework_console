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

import osrframework.entify as entify
import osrframework.utils.regexp_selection as regexp_selection
import osrframework.utils.configuration as configuration
import osrframework.utils.general as general

import osrframework_console.lib.utils as utils
from osrframework_console.lib.interface import OSRFConsoleUtil


class OSRFConsoleEntify(OSRFConsoleUtil):
    """
    Class that controls an interactive entify program.
    """
    # Setting up the name of the module
    UNAME = "entify"

    intro = """
    Loading """ + UNAME + """..."""

    description = """
    A tool to look for known regular expressions in remote or local resources."""

    # Defining the prompt
    prompt = general.emphasis('\nosrf (' + UNAME + ') > ')
    # Defining the character to create hyphens
    ruler = '-'

    # Defining the configuration for this module
    CONFIG = {}
    DEFAULT_VALUES = configuration.returnListOfConfigurationValues("entify")

    # Defining the configuration for this module
    CONFIG = {}
    CONFIG["URL"] = {
        "DESCRIPTION" : "The URL to be checked.",
        "CURRENT_VALUE" : None,
        "DEFAULT_VALUE" : None,
        "REQUIRED" : True,
        "OPTIONS" : []
    }
    CONFIG["REGEXP"] = {
        "DESCRIPTION" : "The regular expressions to be checked.",
        "CURRENT_VALUE" : "all",
        "DEFAULT_VALUE" : "all",
        "REQUIRED" : False,
        "OPTIONS" : regexp_selection.getAllRegexpNames(),
    }
    CONFIG["OUTPUT"] = {
        "DESCRIPTION" : "The path to the output folder where the files will be created.",
        "CURRENT_VALUE" : DEFAULT_VALUES["output_folder"],
        "DEFAULT_VALUE" : DEFAULT_VALUES["output_folder"],
        "REQUIRED" : False,
        "OPTIONS" : []
    }
    CONFIG["EXTENSION"] = {
        "DESCRIPTION" : "The default extension of the files to be written.",
        "CURRENT_VALUE" : DEFAULT_VALUES["extension"],
        "DEFAULT_VALUE" : DEFAULT_VALUES["extension"],
        "REQUIRED" : False,
        "OPTIONS" : ['csv', 'xls', 'xlsx', 'json', 'gml']
    }

    def _getParams(self):
        """
        Function that creates the array with the params of this function

        Returns:
        --------
            list: A list of the params that can be used
        """
        # Creating the parameters as if they were created using the command line
        params = [
            "-u", self.CONFIG["URL"]["CURRENT_VALUE"],
            "-r" ] + self.CONFIG["REGEXP"]["CURRENT_VALUE"] + [
            "-o", self.CONFIG["OUTPUT"]["CURRENT_VALUE"],
            "-e" ] + self.CONFIG["EXTENSION"]["CURRENT_VALUE"]

        return params

    def do_run(self, line):
        """
        Command that send the order to the framework to launch this util

        Args:
        -----
            line: The string of the line typed.
        """
        # Checking if all the required parameters have been set
        if self._checkIfRequiredAreSet():
            print(general.info("\nCollecting the options set by the user...\n"))
            # Getting the parser...
            parser = entify.getParser()

            # Generating the parameters
            params = self._getParams()

            args = parser.parse_args(params)

            print(general.info("\nLaunching " + self.UNAME + " with the following parameters:") + general.emphasis("\t$ " + self.UNAME + " " + utils.listToString(params) + "\n"))

            try:
                entify.main(args)
            except Exception as e:
                print(general.error("\n[!!] ERROR. Something happened when launching the utility. Type 'show options' to check the parameters.\n"))
                print(general.error("Traceback: " + str(e)))
        else:
            print(general.error("\n[!!] ERROR. There are required parameters which have not been set."))
            self.do_show("options")
        print(general.success("Execution ended successfully."))
