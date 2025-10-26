from odoo import models, fields
from datetime import datetime
from dateutil.relativedelta import relativedelta 

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = 'Estate Property'

    name = fields.Char(string="Title", size=10)
    description = fields.Text(string="Description")
    postcode = fields.Char(string="Postcode", size=10)
    date_availability = fields.Date(default=datetime.now() + relativedelta(months=3) , copy=False, string="Available From") # 3 months from current date
    expected_price = fields.Float(string="Expected Price")
    selling_price = fields.Float(readonly=True, copy=False, string="Selling Price")
    bedrooms = fields.Integer(default=2, string="Bedrooms")
    living_area = fields.Integer(string="Living Area (sqm)")
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection([
        ('north', 'North'),
        ('south', 'South'),
        ('east', 'East'),
        ('west', 'West')
    ], string="Garden Orientation")
    state =  fields.Selection([
        ('new', 'New'),
        ('offer_received', 'Offer Received'),
        ('offer_accepted', 'Offer Accepted'),
        ('sold', 'Sold'),
        ('canceled', 'Canceled')
    ], default='new', string="Status", required=True)