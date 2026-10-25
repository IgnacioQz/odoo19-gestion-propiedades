from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    propiedad_ids = fields.One2many(
        'cb.propiedad', 'partner_id', string='Propiedades')
    propiedad_count = fields.Integer(
        string='N° de propiedades', compute='_compute_propiedad_count')

    @api.depends('propiedad_ids')
    def _compute_propiedad_count(self):
        for partner in self:
            partner.propiedad_count = len(partner.propiedad_ids)

    def action_ver_propiedades(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Propiedades',
            'res_model': 'cb.propiedad',
            'view_mode': 'list,form',
            'domain': [('partner_id', '=', self.id)],
            'context': {'default_partner_id': self.id},
        }
