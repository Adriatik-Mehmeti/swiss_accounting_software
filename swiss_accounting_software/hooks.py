app_name = "swiss_accounting_software"
app_title = "Swiss Accounting Software"
app_publisher = "Adriatik Mehmeti"
app_description = "Accounting app for Schweiz"
app_email = "mehmetiadriatik0@gmail.com"
app_license = "mit"

fixtures = [
    {"doctype": "Custom Field", "filters": [["module", "in", ["Module Tax", "Module QR Code", "Camt Erpnext", "Abacus Export" ]]]}    
]

# Apps
# ------------------

#required_apps = ["frappe", "erpnext", "hrms"]

# Each item in the list will be shown as an app in the apps page
add_to_apps_screen = [
 	{
 		"name": "swiss_accounting_software",
 		"logo": "/assets/swiss_accounting_software/img/logo.svg",
 		"title": "Swiss Accounting",
 		"route": "/app/swiss-accounting",
 		"has_permission": "swiss_accounting_software.check_app_permission",
 	}
 ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/swiss_accounting_software/css/swiss_accounting_software.css"
#app_include_css = "desk_swiss_accounting_software.bundle.css"
app_include_js = "swiss_accounting_app.bundle.js"

# include js, css files in header of web template
web_include_css = "swiss_accounting_software.bundle.css"
web_include_js = "swiss_accounting_software.bundle.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "swiss_accounting_software/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
doctype_js = {"Bank Statement Import" : "public/js/doctype/bank_statement_import.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "swiss_accounting_software/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "swiss_accounting_software.utils.jinja_methods",
# 	"filters": "swiss_accounting_software.utils.jinja_filters"
# }

# Installation
# ------------

before_install = "swiss_accounting_software.install.before_install"
after_install = "swiss_accounting_software.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "swiss_accounting_software.uninstall.before_uninstall"
# after_uninstall = "swiss_accounting_software.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "swiss_accounting_software.utils.before_app_install"
# after_app_install = "swiss_accounting_software.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "swiss_accounting_software.utils.before_app_uninstall"
# after_app_uninstall = "swiss_accounting_software.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "swiss_accounting_software.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

override_doctype_class = {
	"Sales Invoice": "swiss_accounting_software.overrides.sales_invoice.SalesInvoiceCustom",
	"Company": "swiss_accounting_software.overrides.company.CompanyCustom"
}

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }
doc_events = {
    "Abacus Export": {
        "on_submit": "swiss_accounting_software.attach_xml",
    }, 
    "Bank Transaction": {
        "on_submit": "swiss_accounting_software.camt_erpnext.bank_transaction_auto_match.bank_transaction_auto_match"
    },
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"swiss_accounting_software.tasks.all"
# 	],
# 	"daily": [
# 		"swiss_accounting_software.tasks.daily"
# 	],
# 	"hourly": [
# 		"swiss_accounting_software.tasks.hourly"
# 	],
# 	"weekly": [
# 		"swiss_accounting_software.tasks.weekly"
# 	],
# 	"monthly": [
# 		"swiss_accounting_software.tasks.monthly"
# 	],
# }

scheduler_events = {

 	"daily": [
 		"swiss_accounting_software.module_payroll.doctype.hours_calculation.hours_calculation.enqueue_hours_calculation"
 	]
}

# Testing
# -------

# before_tests = "swiss_accounting_software.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "swiss_accounting_software.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "swiss_accounting_software.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["swiss_accounting_software.utils.before_request"]
# after_request = ["swiss_accounting_software.utils.after_request"]

# Job Events
# ----------
# before_job = ["swiss_accounting_software.utils.before_job"]
# after_job = ["swiss_accounting_software.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"swiss_accounting_software.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

