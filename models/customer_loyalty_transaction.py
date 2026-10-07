from odoo import fields, models


class CustomerLoyaltyTransaction(models.Model):
    _inherit = 'loyalty.history'

    customer_id = fields.Many2one(
        comodel_name='res.partner',
        string='Khách hàng',
        related='card_id.partner_id',
        store=True,
        index=True,
        readonly=True,
    )
    appointment_id = fields.Many2one(
        comodel_name='spa.appointment',
        string='Lịch hẹn Spa',
        ondelete='set null',
        index=True,
    )

