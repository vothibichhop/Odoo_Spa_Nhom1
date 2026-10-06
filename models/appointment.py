from odoo import fields, models


class SpaAppointment(models.Model):
    _name = 'spa.appointment'
    _description = 'Appointment'

    customer_id = fields.Many2one('spa.customer', string='Customer', required=True)
    service_id = fields.Many2one('spa.service', string='Service', required=True)
    appointment_date = fields.Date(string='Appointment Date', required=True)
    start_time = fields.Float(string='Start Time')
    end_time = fields.Float(string='End Time')
    status = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('checked_in', 'Checked In'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
        ('cancelled', 'Cancelled'),
    ], default='draft', string='Status')
    note = fields.Text(string='Notes')
