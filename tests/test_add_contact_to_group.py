def test_add_contact_in_first_group(app, db, json_contacts, check_ui):
    groups = db.get_group_list()
    if len(groups) == 0:
        app.group.create_if_not_exist()
        groups = db.get_group_list()
    group = groups[0]
    contacts_in_group_before = db.get_contacts_from_group(group)
    contact = json_contacts
    contact.id_contact = app.contact.get_next_id(db.get_contact_list())
    app.contact.create_in_first_group(contact)
    contacts_in_group_after = db.get_contacts_from_group(group)
    assert len(contacts_in_group_before) + 1 == len(contacts_in_group_after)
    contacts_in_group_before.append(contact)
    assert sorted(contacts_in_group_before) == sorted(contacts_in_group_after)
