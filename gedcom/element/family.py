# -*- coding: utf-8 -*-

# Python GEDCOM Parser
#
# Copyright (C) 2018 Damon Brodie (damon.brodie at gmail.com)
# Copyright (C) 2018-2019 Nicklas Reincke (contact at reynke.com)
# Copyright (C) 2016 Andreas Oberritter
# Copyright (C) 2012 Madeleine Price Ball
# Copyright (C) 2005 Daniel Zappala (zappala at cs.byu.edu)
# Copyright (C) 2005 Brigham Young University
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#
# Further information about the license: http://www.gnu.org/licenses/gpl-2.0.html

"""GEDCOM element consisting of tag `gedcom.tags.GEDCOM_TAG_FAMILY`"""

from gedcom.element.element import Element
import gedcom.tags


class NotAnActualFamilyError(Exception):
    pass


class FamilyElement(Element):

    def get_tag(self):
        return gedcom.tags.GEDCOM_TAG_FAMILY

    @property
    def HUSB(self):
        spouse_list = self.find_by_tag('HUSB')
        if len(spouse_list) > 0:
            return self.find(spouse_list[0].value)
        else:
            return None

    @property
    def WIFE(self):
        spouse_list = self.find_by_tag('WIFE')
        if len(spouse_list) > 0:
            return self.find(spouse_list[0].value)
        else:
            return None
