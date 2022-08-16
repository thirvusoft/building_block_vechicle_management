from . import __version__ as app_version

app_name = "building_block_vechicle_management"
app_title = "Building Block Vehicle Management"
app_publisher = "Thirvusoft"
app_description = "Building Block Vehicle Management"
app_icon = "octicon:bug-16"
app_color = "black"
app_email = "info@thirvusoft.in"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/building_block_vechicle_management/css/building_block_vechicle_management.css"
# app_include_js = "/assets/building_block_vechicle_management/js/building_block_vechicle_management.js"

# include js, css files in header of web template
# web_include_css = "/assets/building_block_vechicle_management/css/building_block_vechicle_management.css"
# web_include_js = "/assets/building_block_vechicle_management/js/building_block_vechicle_management.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "building_block_vechicle_management/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
doctype_js = {
    "Vehicle Log":"/custom/js/vehicle_log.js",
    "Vehicle":"/custom/js/vehicle.js",
    }
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "building_block_vechicle_management.install.before_install"
# after_install = "building_block_vechicle_management.install.after_install"
after_install = "building_block_vechicle_management.after_install.after_install"

# Uninstallation
# ------------

# before_uninstall = "building_block_vechicle_management.uninstall.before_uninstall"
# after_uninstall = "building_block_vechicle_management.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "building_block_vechicle_management.notifications.get_notification_config"

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

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

doc_events = {
	"Vehicle Log":{
		"on_update_after_submit": "building_block_retail.building_block_retail.custom.py.vehicle_log.onsubmit",
		"on_submit": ["building_block_retail.building_block_retail.custom.py.vehicle_log.onsubmit",
					  "building_block_retail.building_block_retail.custom.py.vehicle_log.update_transport_cost",
					  "building_block_retail.building_block_retail.custom.py.vehicle_log.vehicle_log_draft"],
		"on_cancel":["building_block_retail.building_block_retail.custom.py.vehicle_log.onsubmit",
					 "building_block_retail.building_block_retail.custom.py.vehicle_log.update_transport_cost"],
		"validate": "building_block_retail.building_block_retail.custom.py.vehicle_log.validate"
	},
	"Vehicle":{
        "validate":"building_block_retail.building_block_retail.custom.py.vehicle.reference_date",
    },
 "Delivery Note":{
  		"before_submit":"building_block_retail.building_block_retail.custom.py.vehicle_log.vehicle_log_creation"
	}
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"building_block_vechicle_management.tasks.all"
# 	],
# 	"daily": [
# 		"building_block_vechicle_management.tasks.daily"
# 	],
# 	"hourly": [
# 		"building_block_vechicle_management.tasks.hourly"
# 	],
# 	"weekly": [
# 		"building_block_vechicle_management.tasks.weekly"
# 	]
# 	"monthly": [
# 		"building_block_vechicle_management.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "building_block_vechicle_management.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "building_block_vechicle_management.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "building_block_vechicle_management.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

user_data_fields = [
	{
		"doctype": "{doctype_1}",
		"filter_by": "{filter_by}",
		"redact_fields": ["{field_1}", "{field_2}"],
		"partial": 1,
	},
	{
		"doctype": "{doctype_2}",
		"filter_by": "{filter_by}",
		"partial": 1,
	},
	{
		"doctype": "{doctype_3}",
		"strict": False,
	},
	{
		"doctype": "{doctype_4}"
	}
]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"building_block_vechicle_management.auth.validate"
# ]

# Translation
# --------------------------------

# Make link fields search translated document names for these DocTypes
# Recommended only for DocTypes which have limited documents with untranslated names
# For example: Role, Gender, etc.
# translated_search_doctypes = []
