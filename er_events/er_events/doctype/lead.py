# -*- coding: utf-8 -*-
# Copyright (c) 2017, laugusto and contributors
# For license information, please see license.txt
from __future__ import unicode_literals
import frappe
from frappe.model.document import Document


@frappe.whitelist()
def attribute_event(doctype, docname):
    lead_doc = frappe.get_doc(doctype, docname)
    to_do = frappe.new_doc('ToDo')
    to_do.status = 'Open'
    to_do.priority = 'Medium'
    to_do.date = lead_doc.contact_date
    to_do.owner = lead_doc.contact_by
    to_do.assigned_by = lead_doc.owner
    to_do.description = 'Contatar {} {}'.format(lead_doc.lead_name, lead_doc.company_name)
    to_do.reference_type = 'Event'
    to_do.reference_name = frappe.db.get_value("Event", filters={"starts_on": lead_doc.contact_date}, fieldname=["name"])
    to_do.save()
    return to_do