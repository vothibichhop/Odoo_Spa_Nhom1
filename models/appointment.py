from odoo import fields, models


class SpaAppointment(models.Model):
    _name = 'spa.appointment'
    _description = 'Lịch hẹn và liệu trình Spa'

    customer_id = fields.Many2one(
        'res.partner',
        string='Khách hàng',
        required=True,
        domain=[('is_spa_customer', '=', True)],
        ondelete='restrict',
    )
    service_id = fields.Many2one('spa.service', string='Dịch vụ/liệu trình', required=True)
    appointment_date = fields.Date(string='Ngày hẹn', required=True)
    start_time = fields.Float(string='Giờ bắt đầu')
    end_time = fields.Float(string='Giờ kết thúc')
    status = fields.Selection([
        ('draft', 'Nháp'),
        ('confirmed', 'Đã xác nhận'),
        ('checked_in', 'Đã đến'),
        ('in_progress', 'Đang thực hiện'),
        ('done', 'Hoàn thành'),
        ('cancelled', 'Đã hủy'),
    ], default='draft', string='Trạng thái')
    note = fields.Text(string='Ghi chú')
