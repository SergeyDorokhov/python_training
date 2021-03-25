import random


def test_delete_contact_from_group(app, db, json_contacts, check_ui):
    groups = db.get_group_list()
    groups_with_contacts = db.get_group_with_contacts()
    if len(groups) == 0:
        app.group.create_if_not_exist()
    if len(groups_with_contacts) == 0:
        contact = json_contacts
        contact.id_contact = app.contact.get_next_id(db.get_contact_list())
        app.contact.create_in_first_group(contact)
    groups_with_contacts = db.get_group_with_contacts()
    group = random.choice(groups_with_contacts)
    contact = random.choice(db.get_contacts_from_group(group))
    contacts_before = db.get_contacts_from_group(group)
    app.contact.delete_contact_by_id(contact.id_contact)
    contacts_after = db.get_contacts_from_group(group)
    assert len(contacts_before) - 1 == len(contacts_after)
    contacts_before.remove(contact)
    assert contacts_before == contacts_after
