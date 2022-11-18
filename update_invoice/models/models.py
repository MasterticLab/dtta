from odoo import models, fields, api

class QRCode_Addon(models.Model):
    _inherit = "account.move.line"


    reference_arti = fields.Char(string="Reference")
    par_cours = fields.Char("Parcours")
    class_a = fields.Char(string="Class",tracking=True)
    design = fields.Char(string="Designation")
    de_billet = fields.Char(string="N'De Billet")
    com = fields.Float(string="Comission")
    puht = fields.Float(string="P.U.HT")
    puttc = fields.Float(string="P.U.TTc")
    cost=fields.Float(string="Cost")



class cost_product(models.Model):
    _inherit="account.move"

    cost=fields.Float(string="Cost",readonly=True,store=True,compute="_compute_cost")
    margin=fields.Float(string='Margin',compute="_compute_margin")

    @api.depends("invoice_line_ids")
    def _compute_cost(self):
        sum=0.0
        for r in self.invoice_line_ids:
            sum+=r.cost

        self.cost=sum
    @api.depends('invoice_line_ids')
    def _compute_margin(self):
        sum=0.0
        sum=self.amount_untaxed-self.cost
        self.margin=sum












