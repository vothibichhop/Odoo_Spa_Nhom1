from odoo import fields, models
from odoo.exceptions import AccessError, UserError


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    spa_appointment_id = fields.Many2one(
        'spa.appointment',
        string='Lịch hẹn Spa',
        readonly=True,
        copy=False,
        ondelete='restrict',
    )

    def action_spa_confirm_payment(self):
        self.ensure_one()
        if not self.env.user.has_group('spa.group_spa_billing_user'):
            raise AccessError(
                'Bạn cần quyền Spa Billing User để xác nhận thanh toán.'
            )
        if not self.spa_appointment_id:
            raise UserError('Đơn hàng này không liên kết với lịch hẹn Spa.')

        if self.state in ('draft', 'sent'):
            self.action_confirm()
        elif self.state != 'sale':
            raise UserError(
                'Chỉ có thể xác nhận thanh toán cho đơn hàng ở trạng thái báo giá '
                'hoặc đã xác nhận.'
            )

        invoice = self.invoice_ids.filtered(
            lambda move: move.move_type == 'out_invoice' and move.state != 'cancel'
        )[:1]
        if not invoice:
            invoice = self._create_invoices()
        if not invoice:
            raise UserError('Không thể tạo hóa đơn từ đơn hàng này.')

        invoice.action_post()
        self.spa_appointment_id.invoice_id = invoice[:1]
        self.spa_appointment_id._award_loyalty_points()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Hóa đơn thanh toán',
            'res_model': 'account.move',
            'view_mode': 'form',
            'res_id': invoice[:1].id,
            'target': 'current',
        }
