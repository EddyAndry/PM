###################################################################################
# 
#    Copyright (C) 2018 MuK IT GmbH
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###################################################################################

import logging

from odoo import models, api

from odoo.addons.dcs_utils.tools import patch

_logger = logging.getLogger(__name__)

@api.multi
@patch.monkey_patch_model(models.BaseModel)
def unlink(self):
    oids = []
    for name in self._fields:
        field = self._fields[name]
        if field.type == 'lobject' and field.store:
            for record in self:
                oid = record.with_context({'oid': True})[name]
                if oid:
                    oids.append(oid)
    unlink.super(self)
    for oid in oids:
        self.env.cr._cnx.lobject(oid, 'rb').unlink()