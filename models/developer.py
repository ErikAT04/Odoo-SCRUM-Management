from odoo import models, fields, api


class developer(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'

    is_dev = fields.Boolean(default=True, readonly=True)
    technologies = fields.Many2many('manageerik.technology', relation='developer_technologies', column1='developers', column2='technologies')
