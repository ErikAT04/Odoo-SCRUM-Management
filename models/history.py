from odoo import models, fields, api

class history(models.Model):
    _name = 'manageerik.history'
    _description = 'manageerik.history'

    id = fields.Integer()
    name = fields.Char(required=True)
    description = fields.Text()