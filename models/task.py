from odoo import models, fields, api

class task(models.Model):
    _name = 'manageerik.task'
    _description = 'manageerik.task'

    id = fields.Integer()
    name = fields.Char(required=True)
    code = fields.Char(readonly=True)
    description = fields.Text()
    start_date = fields.Datetime(required=True),
    duration = fields.Integer(),
    end_date = fields.Datetime(readonly=True)