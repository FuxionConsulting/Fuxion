# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    #IVA
    allow_vat_wh_outdated = fields.Boolean(
        string="Retención Automática de IVA", readonly=False)

    # ISLR
    automatic_income_wh = fields.Boolean(
        'Retención Automática de Ingresos', related="company_id.automatic_income_wh", readonly=False)

    calculate_wh_itf = fields.Boolean('Retención automática de ITF', related="company_id.calculate_wh_itf", readonly=False)

    wh_porcentage = fields.Float('% ITF', help="El porcentaje a aplicar para retener", related="company_id.wh_porcentage", readonly=False)

    account_wh_itf_id = fields.Many2one('account.account', string="Cuenta ITF", related="company_id.account_wh_itf_id",
                                        help="Esta cuenta se utilizará en lugar de la predeterminada"
                                             "para generar el asiento del ITF", readonly=False)