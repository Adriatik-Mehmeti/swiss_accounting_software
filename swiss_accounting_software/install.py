import subprocess
import sys
import os
import frappe

def after_install():
    """ Make sure that the accounting dimension for Steuerziffer CH already exists"""
    create_steuerziffer_dimension()

def before_install():
    """Install Python dependencies from requirements.txt before app installation"""
    requirements_path = os.path.join(os.path.dirname(__file__), "requirements.txt")

    if os.path.exists(requirements_path):
        frappe.logger().info(f"Installing dependencies from {requirements_path}...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", requirements_path])
        frappe.logger().info("All dependencies installed successfully.")
    else:
        frappe.logger().warning(f"requirements.txt not found at {requirements_path}")

    if not frappe.db.exists("Letter Head", {"letter_head_name": "Default Letter Header"}):
        template_head = """
        <div class='print-heading'>
            <div style='display:flex;'>

                {% set company_name = doc.company or frappe.db.get_value('Company', {'default_letter_head': 'Default Letter Header'}, 'name') %}

                {% if company_name and frappe.db.exists('Company', company_name) %}
                    {% set h_company = frappe.get_doc('Company', company_name) %}

                    {% set d_link = frappe.db.get_value('Dynamic Link', {
                        'link_doctype': 'Company',
                        'link_name': h_company.name,
                        'parenttype': 'Address'
                    }, 'parent') %}

                    {% if d_link %}
                        {% set company_address = frappe.get_doc('Address', d_link) %}
                    {% else %}
                        {% set company_address = None %}
                    {% endif %}

                    <div class='col-lg-4'>
                        <div class='row'>
                            <h5 class='m-0 p-0'><strong>{{ h_company.company_name }}</strong></h5>
                            {% if company_address %}
                                <p class='text-muted m-0 p-0'>{{ company_address.address_line1 }}</p>
                                <p class='text-muted m-0 p-0'>{{ company_address.pincode }} {{ _(company_address.city) }}</p>
                            {% endif %}
                        </div>
                    </div>

                    <div class='ml-auto col-lg-3'>
                        {% set logo = frappe.db.get_value('Company', h_company.name, 'company_logo') %}
                        {% if logo %}
                            <img class='brand-image' height='100px' src='{{ logo }}'>
                        {% endif %}
                    </div>
                {% endif %}
            </div>
        </div>
        """
        
        frappe.get_doc({
            "doctype": "Letter Head",
            "letter_head_name": "Default Letter Header" ,
            "source": "HTML",
            "content": template_head,
        }).insert(ignore_permissions=True)


def create_steuerziffer_dimension():
    if not frappe.db.exists("Accounting Dimension", {"document_type": "Steuerziffer CH"}):
        
        doc = frappe.get_doc({
            "doctype": "Accounting Dimension",
            "document_type": "Steuerziffer CH",
            "label": "Steuerziffer CH"
        })
        doc.insert(ignore_permissions=True)
        frappe.db.commit()