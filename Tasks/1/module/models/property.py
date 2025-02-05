from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Property(models.Model):
    _name = 'property'
    name = fields.Char(required=1, default='New', size=25)
    description = fields.Text()
    postcode = fields.Char(required=1)
    date_availability = fields.Date()
    expected_price = fields.Float(digits=(0, 5))
    selling_price = fields.Float()
    bedrooms = fields.Integer()
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection([
        # the first value of a tuple is the column name
        # the second value of a tuple is what will be shown to the user
        ('north', 'North'),
        ('south', 'South'),
        ('east', 'East'),
        ('west', 'West'),
    ], default='north')
    owner_id = fields.Many2one('owner')
    tag_ids = fields.Many2many('tag')

    _sql_constraints = [
        ('unique_name', 'unique("name")', 'This name already exists!')
    ]

    @api.constrains('bedrooms')
    def _check_bedrooms_greater_zero(self):
        for rec in self:
            if rec.bedrooms < 1:
                raise ValidationError('Please add a positive number of bedrooms!')


    # @api.model_create_multi
    # def create(self, vals):
    #     res = super(Property, self).create(vals)
    #     print("create method")
    #     return res
    #
    # @api.model
    # def _search(self, domain, offset=0, limit=None, order=None, access_rights_uid=None):
    #     res = super(Property,self)._search(domain, offset=0, limit=None, order=None, access_rights_uid=None)
    #     print("read/search method")
    #     return res
    #
    # def write(self, vals):
    #     res = super(Property, self).write(vals)
    #     print("update/write method")
    #     return res
    #
    # def unlink(self):
    #     res = super(Property, self).unlink()
    #     print("delete/unlink method")
    #     return res