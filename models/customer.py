from odoo import api, fields, models
from odoo.exceptions import ValidationError


class ResPartner(models.Model):
    _inherit = 'res.partner'

    is_spa_customer = fields.Boolean(
        string='Khách hàng Spa',
        default=False,
        copy=False,
        index=True,
    )
    spa_customer_code = fields.Char(
        string='Mã khách hàng',
        copy=False,
        readonly=True,
        index=True,
    )
    customer_code = fields.Char(
        related='spa_customer_code',
        string='Mã khách hàng (tương thích)',
        readonly=False,
        store=True,
    )
    customer_type = fields.Selection(
        [
            ('new', 'Khách hàng mới'),
            ('regular', 'Khách hàng thân thiết'),
            ('vip', 'Khách hàng VIP'),
        ],
        string='Phân loại khách hàng',
    )
    spa_birthday = fields.Date(string='Ngày sinh')
    spa_gender = fields.Selection(
        [('male', 'Nam'), ('female', 'Nữ'), ('other', 'Khác')],
        string='Giới tính',
    )
    spa_skin_type = fields.Selection(
        [
            ('normal', 'Da thường'),
            ('dry', 'Da khô'),
            ('oily', 'Da dầu'),
            ('combination', 'Da hỗn hợp'),
            ('sensitive', 'Da nhạy cảm'),
            ('other', 'Khác'),
        ],
        string='Loại da',
    )
    skin_condition = fields.Text(string='Tình trạng da')
    customer_need = fields.Text(string='Nhu cầu chăm sóc')
    customer_note = fields.Text(string='Lưu ý khách hàng')
    spa_appointment_ids = fields.One2many(
        'spa.appointment',
        'customer_id',
        string='Lịch sử liệu trình',
    )
    spa_appointment_count = fields.Integer(
        string='Số lịch hẹn',
        compute='_compute_spa_appointment_count',
    )

    _sql_constraints = [
        (
            'spa_customer_code_unique',
            'unique(spa_customer_code)',
            'Mã khách hàng Spa phải là duy nhất.',
        ),
    ]

    @api.model_create_multi
    def create(self, vals_list):
        default_is_spa_customer = self.default_get(['is_spa_customer']).get(
            'is_spa_customer',
        )
        for vals in vals_list:
            is_spa_customer = vals.get(
                'is_spa_customer',
                default_is_spa_customer,
            )
            if is_spa_customer and not vals.get('spa_customer_code'):
                code = self.env['ir.sequence'].next_by_code('spa.customer')
                if not code:
                    raise ValidationError(
                        'Không tìm thấy dãy số mã khách hàng Spa.',
                    )
                vals['spa_customer_code'] = code
        return super().create(vals_list)

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
