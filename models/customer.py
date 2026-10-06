from odoo import models, fields
class SpaCustomer(models.Model):
    _name = 'spa.customer'
    _description = 'Khách hàng Spa'
    name = fields.Char(string='Họ và tên',required=True)
    customer_code = fields.Char(string='Mã khách hàng',required=True,copy=False)
    phone = fields.Char(string='Số điện thoại')
    birthday = fields.Date(string='Ngày sinh')
    gender = fields.Selection([('male', 'Nam'),('female', 'Nữ'),('other', 'Khác'),],string='Giới tính')
    address = fields.Text(string='Địa chỉ')
    note = fields.Text(string='Ghi chú')
    active = fields.Boolean(string='Đang hoạt động',default=True)