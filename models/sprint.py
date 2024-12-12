from odoo import models, fields, api

class sprint(models.Model):
    _name = 'manageerik.sprint'
    _description = 'manageerik.sprint'

    id = fields.Integer()
    name = fields.Char(required=True)
    description = fields.Text()
    start_date = fields.Datetime(required=True),
    duration = fields.Integer(),
    end_date = fields.Datetime(readonly=True)