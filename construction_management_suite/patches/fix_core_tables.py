import frappe
from frappe.model.db_schema import DbManager


def execute():
    dbm = DbManager(frappe.db)
    core_doctypes = [
        'Module Def', 'Role', 'User', 'Notification', 'User Role',
        'Installed Applications',
    ]
    for dt in core_doctypes:
        try:
            if not frappe.db.table_exists(dt):
                dbm.sync_doctype_table(dt)
                print(f'Created: {dt}')
            else:
                print(f'Exists:  {dt}')
        except Exception as e:
            print(f'Error {dt}: {e}')
    frappe.db.commit()
