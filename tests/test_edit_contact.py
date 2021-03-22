# -*- coding: utf-8 -*-
import random

from model.contact import Contact


def test_edit_some_contact(app, db, check_ui):
    app.contact.create_if_not_exist()
    list_before = db.get_contact_list()
    edit_contact = random.choice(list_before)
    id = edit_contact.id_contact
    contact = Contact(firstname="new firstname", lastname="new lastname", home_phone=123,
                      mobile_phone=456, work_phone=789)
    contact.id_contact = id
    app.contact.edit_contact_by_id(contact, id)
    assert len(list_before) == len(db.get_contact_list())
    list_before.remove(edit_contact)
    list_before.append(contact)
    list_after = db.get_contact_list()
    assert sorted(list_before) == sorted(list_after)
    if check_ui:
        assert sorted(list_after) == sorted(app.contact.get_list())
