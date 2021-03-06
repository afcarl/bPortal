#######################################################################
# bPortal is a SuiteCRM portal written using django project.

# Copyright (C) 2017-2018 BTACTIC, SCCL
# Copyright (C) 2017-2018 Marc Sanchez Fauste

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#######################################################################

from module_definition import ModuleDefinition
from link_type import LinkType

class Bugs(ModuleDefinition):

    @property
    def name(self):
        return 'Bugs'

    @property
    def contacts_link_type(self):
        return LinkType.RELATIONSHIP

    @property
    def contacts_link_name(self):
        return 'bugs'

    @property
    def accounts_link_type(self):
        return LinkType.RELATIONSHIP

    @property
    def accounts_link_name(self):
        return 'bugs'
