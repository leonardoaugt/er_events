frappe.ui.form.on('Lead', {

    after_save: function (frm) {
        if (frappe.session.user != frm.doc.contact_by) {
            frappe.call({
                method: "er_events.er_events.doctype.lead.attribute_event",
                args: {
                    doctype: frm.doc.doctype,
                    docname: frm.doc.name,
                },
                callback: function (r) {
                    event_name = r.message.reference_name;
                    frappe.show_alert(`Evento ${event_name} criado!`);
                }
            });
        }
    },

});