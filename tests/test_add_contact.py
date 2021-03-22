def test_add_contact(app, db, json_contacts, check_ui):
    contact = json_contacts
    list_before = db.get_contact_list()
    contact.id_contact = app.contact.get_next_id(list_before)
    app.contact.create(contact)
    assert len(list_before) + 1 == len(db.get_contact_list())
    list_after = db.get_contact_list()
    list_before.append(contact)
    assert sorted(list_before) == sorted(list_after)
    if check_ui:
        assert sorted(list_after) == sorted(app.contact.get_list())