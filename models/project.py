from odoo import models, fields, api

class project(models.Model):
    _name = 'manageerik.project'
    _description = 'manageerik.project'

    id = fields.Integer()
    name = fields.Char(required=True)
    description = fields.Text()
