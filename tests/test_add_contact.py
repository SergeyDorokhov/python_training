def test_add_contact(app, json_contacts):
    contact = json_contacts
    list_before = app.contact.get_list()
    contact.id_contact = app.contact.get_next_id(list_before)
    app.contact.create(contact)
    assert len(list_before) + 1 == app.contact.count()
    list_after = app.contact.get_list()
    list_before.append(contact)
    assert sorted(list_before) == sorted(list_after)
