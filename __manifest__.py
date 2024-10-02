# -*- coding: utf-8 -*-
{
    'name': "picking_category_total_quantity",

    'summary': "PRODUCT CATEGORY DEMAND MANAGEMENT AND REPORTING CONFIGURATION",

    'description': """
This module offers real-time visibility into product category Demand and Done automatically updated when products are selected on the delivery line, 
enabling users to make data-driven decisions.
    """,

    'author': "Amzsys",
    'website': "http://www.amzsys.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'stock', 'product'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'views/stock_picking_views.xml',
        'report/report_sockpicking_operations.xml',
    ],
}

