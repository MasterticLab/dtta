from odoo import models, fields, api

class QRCode_Addon(models.Model):
    _inherit = "account.move.line"


    reference_arti = fields.Char(string="Reference")
    par_cours = fields.Char("Parcours")
    class_a = fields.Char(string="Class",tracking=True)
    design = fields.Char(string="Designation")
    de_billet = fields.Integer(string="N'De Billet")
    com = fields.Float(string="Comission")
    puht = fields.Float(string="P.U.HT")
    puttc = fields.Float(string="P.U.TTc")




