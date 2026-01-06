from odoo import models, fields, api

class ResPartnerids(models.Model):
    _inherit = 'res.partner'

    other_id_available = fields.Selection(
    [("yes", "Yes"), ("no", "No")],
    string="Do you have other ID?",
    )

    other_id_type = fields.Selection(
    [
        ("national_id", "National ID"),
        ("passport", "Passport"),
        ("driving_licence", "Driving Licence"),
        ("voter_id", "Voter ID"),
        ("other", "Other"),
    ],
    string="If Yes, what type of ID",
    )
    other_id_name = fields.Char(string="The other ID")
    other_id_number = fields.Char(string="Alternative ID number")
  








