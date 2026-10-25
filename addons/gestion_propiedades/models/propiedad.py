from odoo import api, fields, models
from odoo.exceptions import UserError, ValidationError


class Propiedad(models.Model):
    _name = 'cb.propiedad'
    _description = 'Propiedad'
    _order = 'fecha_publicacion desc, id desc'

    name = fields.Char(string='Título', required=True)
    codigo = fields.Char(string='Código', copy=False)
    tipo = fields.Selection(
        [('casa', 'Casa'), ('departamento', 'Departamento'),
         ('oficina', 'Oficina'), ('terreno', 'Terreno')],
        string='Tipo', default='departamento', required=True)
    estado = fields.Selection(
        [('disponible', 'Disponible'), ('reservada', 'Reservada'),
         ('vendida', 'Vendida')],
        string='Estado', default='disponible', copy=False, required=True)
    precio_uf = fields.Float(string='Precio (UF)')
    superficie_m2 = fields.Float(string='Superficie (m²)')
    fecha_publicacion = fields.Date(
        string='Fecha de publicación', default=fields.Date.context_today)
    notas = fields.Text(string='Notas')
    active = fields.Boolean(default=True)
    partner_id = fields.Many2one(
        'res.partner', string='Propietario', ondelete='restrict')
    agente_id = fields.Many2one(
        'res.users', string='Agente', default=lambda self: self.env.user)
    precio_uf_m2 = fields.Float(
        string='UF por m²', compute='_compute_precio_uf_m2', store=True)

    @api.depends('precio_uf', 'superficie_m2')
    def _compute_precio_uf_m2(self):
        for rec in self:
            rec.precio_uf_m2 = (
                rec.precio_uf / rec.superficie_m2 if rec.superficie_m2 else 0.0)

    @api.constrains('precio_uf', 'superficie_m2')
    def _check_valores(self):
        for rec in self:
            if rec.precio_uf < 0:
                raise ValidationError('El precio no puede ser negativo.')
            if rec.superficie_m2 < 0:
                raise ValidationError('La superficie no puede ser negativa.')

    def action_reservar(self):
        for rec in self:
            if rec.estado != 'disponible':
                raise UserError('Solo se puede reservar una propiedad disponible.')
            rec.estado = 'reservada'

    def action_vender(self):
        for rec in self:
            if rec.estado != 'reservada':
                raise UserError('Solo se puede vender una propiedad reservada.')
            rec.estado = 'vendida'

    def action_disponibilizar(self):
        self.write({'estado': 'disponible'})
