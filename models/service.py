from odoo import fields, models


class SpaService(models.Model):
    _name = 'spa.service'
    _description = 'Service'

    name = fields.Char(string='Service Name', required=True)
    category = fields.Selection([
        ('massage', 'Massage'),
        ('facial', 'Facial'),
        ('hair', 'Hair'),
        ('spa_package', 'Spa Package'),
    ], string='Category')
    duration_minutes = fields.Integer(string='Duration (Minutes)', required=True)
    price = fields.Float(string='Price', required=True)
    description = fields.Text(string='Description')
    active = fields.Boolean(default=True, string='Active')
