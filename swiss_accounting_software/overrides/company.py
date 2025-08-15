import frappe
from erpnext.setup.doctype.company.company import Company

class CompanyCustom(Company):

    def validate(self):
        super().validate()

        if self.is_new() and not self.default_letter_head or not self.default_letter_head:
            if frappe.db.exists("Letter Head", {"letter_head_name": "Default Letter Header"}):
                self.default_letter_head = "Default Letter Header"