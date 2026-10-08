from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    is_spa_customer = fields.Boolean(string='Khách hàng Spa', default=False, copy=False, index=True)
    spa_customer_code = fields.Char(string='Mã khách hàng Spa', copy=False, index=True)
    customer_code = fields.Char(string='Mã khách hàng', copy=False, index=True)
    customer_type = fields.Selection([
        ('new', 'Khách hàng mới'),
        ('regular', 'Khách hàng thường xuyên'),
        ('vip', 'Khách hàng VIP'),
    ], string='Phân loại khách hàng', default='new', tracking=True)
    spa_birthday = fields.Date(string='Ngày sinh')
    spa_gender = fields.Selection(
        [('male', 'Nam'), ('female', 'Nữ'), ('other', 'Khác')], string='Giới tính'
    )
    spa_skin_type = fields.Selection([
        ('normal', 'Da thường'),
        ('dry', 'Da khô'),
        ('oily', 'Da dầu'),
        ('combination', 'Da hỗn hợp'),
        ('sensitive', 'Da nhạy cảm'),
        ('other', 'Khác'),
    ], string='Loại da')
    skin_condition = fields.Text(string='Tình trạng da')
    customer_need = fields.Text(string='Nhu cầu chăm sóc')
    customer_note = fields.Text(string='Lưu ý khách hàng')
    care_note = fields.Text(string='Lưu ý chăm sóc')
    loyalty_point = fields.Integer(string='Điểm tích lũy', default=0, readonly=True, copy=False)
    spa_appointment_ids = fields.One2many(
        'spa.appointment', 'customer_id', string='Lịch sử liệu trình'
    )
    spa_appointment_count = fields.Integer(
        string='Số lịch hẹn', compute='_compute_spa_appointment_count'
    )
    care_need_ids = fields.One2many('customer.care.need', 'partner_id', string='Nhu cầu chăm sóc')
    skin_profile_ids = fields.One2many('customer.skin.profile', 'partner_id', string='Hồ sơ tình trạng da')
    treatment_ids = fields.One2many('customer.treatment', 'partner_id', string='Liệu trình')
    loyalty_transaction_ids = fields.One2many(
        'customer.loyalty.transaction', 'partner_id', string='Lịch sử điểm'
    )

    @api.depends('spa_appointment_ids')
    def _compute_spa_appointment_count(self):
        grouped_data = self.env['spa.appointment']._read_group(
            [('customer_id', 'in', self.ids)],
            ['customer_id'],
            ['__count'],
        )
        counts = {partner.id: count for partner, count in grouped_data}
        for partner in self:
            partner.spa_appointment_count = counts.get(partner.id, 0)

    def action_view_spa_appointments(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Lịch hẹn',
            'res_model': 'spa.appointment',
            'view_mode': 'list,form',
            'domain': [('customer_id', '=', self.id)],
            'context': {'default_customer_id': self.id},
        }
