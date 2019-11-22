# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleOrderInherit(models.Model):
    _inherit = 'res.company'
    hr_salary = fields.Many2one('hr.salary.rule', string="Salary rule", default=lambda self: self._default_salary())
    heure = fields.Float(string='HSUP_EXONERE', related='hr_salary.amount_fix')

    @api.model
    def _default_salary(self):
    	amount = self.env['hr.salary.rule'].search([('name','=','Sup')])
    	return amount


    
    # @api.onchange('heure')
    # def handed(self):
    # 	if self.heure:
    # 		self.hr_salary['amount_fix'].update(self.heure)
    # 		# amount.update({'amount_fix' : self.heure})
    # 	print "&"*50
    # 	print self.heure
    # 	print self.hr_salary.amount_fix
