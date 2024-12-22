from odoo import models, fields, api

class techonology(models.Model):
    _name = 'manageerik.technology'
    _description = 'manageerik.technology'

    id = fields.Integer()
    name = fields.Char(required=True)
    description = fields.Text()
    image = fields.Image()
    tasks = fields.Many2many("manageerik.task", string="Tasks", relation = "techs_tasks", column1 = "tasks", column2 = "technologies")