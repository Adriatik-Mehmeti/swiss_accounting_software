from erpnext.controllers.selling_controller import SellingController
from erpnext.accounts.doctype.sales_invoice.sales_invoice import SalesInvoice
from swiss_accounting_software import text_to_qr
import frappe
from frappe.utils.file_manager import delete_file

class SalesInvoiceCustom(SalesInvoice):

    def validate(self):
        super().validate()

        if self.custom_invoice_reference:
            file_doc = frappe.get_doc("File", {"file_url": self.custom_qr_code_generated})
            delete_file(self.custom_qr_code_generated)
            frappe.delete_doc(
                "File", 
                file_doc.name, 
                ignore_permissions=True,  
            )

        if not self.custom_invoice_reference:
            self.reference()
        self.custom_qr_code_generated = text_to_qr(self.generate_swiss_qr_data(), b_64=False)

    
    def generate_swiss_qr_data(self):
        company = frappe.get_doc("Company", self.company)
        company_address = frappe.get_doc("Address", self.company_address)
        customer = frappe.get_doc("Customer", self.customer)
        customer_address = frappe.get_doc("Address", self.customer_address)

        payload = "\n".join([
            "SPC",               # Swiss Payments Code
            "0200",              # Version
            "1",                 # UTF-8
            self.custom_c_qr_iban.replace(" ", ""),   # IBAN without spaces
            company.company_name,
            company_address.address_line1,
            f"{company_address.pincode} {company_address.city}",
            company_address.pincode or "CH",
            "",                  # Ultimate creditor empty
            f"{self.total:.2f}",  # Amount
            self.currency,
            customer.customer_name,
            customer_address.address_line1,
            f"{customer_address.pincode} {customer_address.city}",
            customer_address.pincode or "CH",
            "QRR",               # Reference type
            self.custom_invoice_reference,
            "",                  # Additional info
            "EPD"                # End of payment data
        ])

        return payload
    
    def before_save(self):
        super().before_save()
        self.reference()
 
    
    def reference(self):
        # Remove non-numeric and pad to 26 digits
        base = "".join(filter(str.isdigit, self.name)).zfill(26)

        table = [0, 9, 4, 6, 8, 2, 7, 1, 3, 5]
        carry = 0
        for digit in base:
            carry = table[(carry + int(digit)) % 10]
        checksum = (10 - carry) % 10

        self.custom_invoice_reference = base + str(checksum)