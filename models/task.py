from odoo import models, fields, api
import datetime

class task(models.Model):
    _name = 'manageerik.task'
    _description = 'manageerik.task'

    id = fields.Integer()
    name = fields.Char(required=True)
    code = fields.Char(compute="_get_code", store = False)
    description = fields.Text()
    start_date = fields.Datetime(required=True)
    duration = fields.Integer()
    end_date = fields.Datetime(compute="_get_end_date", store=True)

    history = fields.Many2one("manageerik.history", required = True, ondelete = "cascade", string="History", help="aaaa")
    technologies = fields.Many2many("manageerik.technology", string="Techs", relation = "techs_tasks", column1 = "technologies", column2 = "tasks")
    sprint = fields.Many2one("manageerik.sprint", ondelete = "cascade", string="Sprint", compute="_get_sprint", store = True)

    @api.depends('name')
    def _get_code(self):
        for task in self:
            if task.name == False:
                task.code = "TSK_noCode"
            else:
                task.code = f"TSK_{task.name}"

    @api.depends('start_date', 'duration')
    def _get_end_date(self):
        for task in self:
            if isinstance(task.start_date, datetime.datetime) and task.duration > 0:
                task.end_date = task.start_date + datetime.timedelta(days=task.duration)
            else:
                task.end_date = task.start_date

    @api.depends('history')
    def _get_sprint(self):
        for task in self:
            sprints = self.env['manageerik.sprint'].search([('project.id', '=', task.history.project.id)])
            found = False
            for sprint in sprints:
                if isinstance(sprint.end_date, datetime.datetime) and sprint.end_date > datetime.datetime.now():
                    task.sprint = sprint
                    found = True
            if not found:
                task.sprint = False