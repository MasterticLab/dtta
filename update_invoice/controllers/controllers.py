# -*- coding: utf-8 -*-
# from odoo import http


# class PurReportBarcode(http.Controller):
#     @http.route('/pur_report_barcode/pur_report_barcode/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/pur_report_barcode/pur_report_barcode/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('pur_report_barcode.listing', {
#             'root': '/pur_report_barcode/pur_report_barcode',
#             'objects': http.request.env['pur_report_barcode.pur_report_barcode'].search([]),
#         })

#     @http.route('/pur_report_barcode/pur_report_barcode/objects/<model("pur_report_barcode.pur_report_barcode"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('pur_report_barcode.object', {
#             'object': obj
#         })
