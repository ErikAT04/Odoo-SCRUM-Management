from odoo import models, fields, api

class project(models.Model):
    _name = 'manageerik.project'
    _description = 'manageerik.project'

    id = fields.Integer()
    name = fields.Char(required=True)
    description = fields.Text()

    histories = fields.One2many(string="Histories", comodel_name="manageerik.history", inverse_name="project", readonly=True)
    sprints = fields.One2many(string="Sprints", comodel_name="manageerik.sprint", inverse_name="project", readonly=True)
    totaltasks = fields.Integer(string="Total Tasks", compute = "_get_tasks")


    def _get_tasks(self):
        for project in self:
            project.totaltasks = 0
            num = 0
            for sprint in project.sprints:
                for task in sprint.tasks:
                    num = num + 1
            project.totaltasks = num
                
