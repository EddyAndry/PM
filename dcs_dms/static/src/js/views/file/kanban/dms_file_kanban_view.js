/**********************************************************************************
* 
*    Copyright (C) 2017 MuK IT GmbH
*
*    This program is free software: you can redistribute it and/or modify
*    it under the terms of the GNU Affero General Public License as
*    published by the Free Software Foundation, either version 3 of the
*    License, or (at your option) any later version.
*
*    This program is distributed in the hope that it will be useful,
*    but WITHOUT ANY WARRANTY; without even the implied warranty of
*    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
*    GNU Affero General Public License for more details.
*
*    You should have received a copy of the GNU Affero General Public License
*    along with this program.  If not, see <http://www.gnu.org/licenses/>.
*
**********************************************************************************/

odoo.define('dcs_dms_views.FileKanbanView', function (require) {
"use strict";

var core = require('web.core');
var registry = require('web.view_registry');

var KanbanView = require('web.KanbanView');

var FileKanbanRenderer = require('dcs_dms_views.FileKanbanRenderer');
var FileKanbanController = require('dcs_dms_views.FileKanbanController');

var _t = core._t;
var QWeb = core.qweb;

var FileKanbanView = KanbanView.extend({
	config: _.extend({}, KanbanView.prototype.config, {
		Renderer: FileKanbanRenderer,
        Controller: FileKanbanController,
    }),
});

registry.add('file_kanban', FileKanbanView);

return FileKanbanView;

});
