#-*- coding: utf-8 -*-
import logging

from odoo import models, fields, api, exceptions

logger = logging.getLogger(__name__)

class ProductTemplate(models.Model):
    _inherit = 'product.template'


#    _sql_constraints = [
#        ('sku_unique',
#         'UNIQUE(default_code)',
#         "This SKU already exists for another product. Please enter a new (non-existing) SKU"),
#    ]



    
    @api.constrains('default_code')
    def _check_sku_unique(self):
        print("Check SKU")
        logging.info("--- Prod Mgmt --- : Entering sku check ")
        for rec in self:
            if rec.default_code:
                logging.info("--- Prod Mgmt --- : SKU is %s for  product %s " % (str(rec.default_code) , str(rec.id)))
                prod_template = self.env['product.template'].search([
                ('default_code', '=', rec.default_code),('id','!=',rec.id)
                ],limit=1)

                if prod_template:
                    logging.info("--- Prod Mgmt --- : SKU exists for Prod template : %s " %str(prod_template.id))
                    raise exceptions.ValidationError("SKU [ %s ] already exists for another product. Please enter a new (non-existing) SKU" %(rec.default_code ))
                else:
                    logging.info("--- Prod Mgmt --- : SKU : Prod template not found")
            else:
                logging.info("--- Prod Mgmt --- : SKU : Not found " )
                logging.info("--- Prod Mgmt --- : SKU : Not found " )
