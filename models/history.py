from odoo import models, fields, api

class history(models.Model):
    _name = 'manageerik.history'
    _description = 'manageerik.history'

    id = fields.Integer()
    name = fields.Char(required=True)
    description = fields.Text()

    project = fields.Many2one("manageerik.project", ondelete = "cascade", string="Project")
    tasks = fields.One2many(string = "Tasks", comodel_name="manageerik.task", inverse_name="history", readonly=True)

    used_technologies = fields.Many2many("manageerik.technology", compute="_get_used_technologies")
    
    def _get_used_technologies(self):
            for history in self:
                technologies = None
                for task in history.tasks:
                    if not technologies:
                        technologies = task.technologies
                    else:
                        technologies = technologies + task.technologies
                history.used_technologies = technologies