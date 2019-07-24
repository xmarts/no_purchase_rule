# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ProcurementGroup(models.Model):
    _name = 'procurement.group'
    _inherit = 'procurement.group'

    @api.model
    def run(self, product_id, product_qty, product_uom, location_id, name, origin, values):
        """ Method used in a procurement case. The purpose is to supply the
        product passed as argument in the location also given as an argument.
        In order to be able to find a suitable location that provide the product
        it will search among stock.rule.
        """
        values.setdefault('company_id', self.env['res.company']._company_default_get('procurement.group'))
        values.setdefault('priority', '1')
        values.setdefault('date_planned', fields.Datetime.now())
        rule = self._get_rule(product_id, location_id, values)
        if not rule:
            raise UserError(
                _('No procurement rule found in location "%s" for product "%s".\n Check routes configuration.') % (
                location_id.display_name, product_id.display_name))
        action = 'pull' if rule.action == 'pull_push' else rule.action
        print("Action: ", action)
        print("Values: ", values)
        print("Origin: ", origin)
        sa = self.env['sale.order'].search([('name', '=', origin)], limit=1)
        print("Sale: ", sa)
        if sa and action == 'buy' and product_qty <= product_id.virtual_available:
            print('Viene de venta ', sa.name, product_qty, product_id.virtual_available)
        else:
            if hasattr(rule, '_run_%s' % action):
                getattr(rule, '_run_%s' % action)(product_id, product_qty, product_uom, location_id, name, origin,
                                                  values)
            else:
                _logger.error("The method _run_%s doesn't exist on the procument rules" % action)
        return True