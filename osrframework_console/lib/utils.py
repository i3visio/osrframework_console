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

def listToString(array):
    """
    A method that converts a list onto a string

    Args:
    -----
        array: A list of strings.

    Returns:
    --------
        A string containing the elements of the list separated by a ' '.
    """
    if isinstance(array, list):
        aux = ""
        for e in array:
            aux += e + " "
        return aux
    return str(array)
