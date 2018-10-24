# -*- encoding: utf-8 -*-

import logging

from docutils import nodes
from docutils.core import publish_string
from docutils.transforms import Transform, writer_aux
from docutils.writers.html4css1 import Writer

from odoo import tools

_logger = logging.getLogger(__name__)

class ReStructuredTextFilterMessages(Transform):
    default_priority = 870
    def apply(self):
        for node in self.document.traverse(nodes.system_message):
            node.parent.remove(node)

class ReStructuredTextWriter(Writer):
    def get_transforms(self):
        return [ReStructuredTextFilterMessages, writer_aux.Admonitions]

def rst2html(content):
    overrides = {
        'embed_stylesheet': False,
        'doctitle_xform': False,
        'output_encoding': 'unicode',
        'xml_declaration': False,
    }
    output = publish_string(content, settings_overrides=overrides, writer=ReStructuredTextWriter())
    return tools.html_sanitize(output)