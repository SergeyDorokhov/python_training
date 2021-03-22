# -*- coding: utf-8 -*-
import random


def test_delete_some_contact(app, db, check_ui):
    app.contact.create_if_not_exist()
    list_before = db.get_contact_list()
    contact = random.choice(list_before)
    app.contact.delete_contact_by_id(contact.id_contact)
    assert len(list_before) - 1 == len(db.get_contact_list())
    list_after = db.get_contact_list()
    list_before.remove(contact)
    assert list_before == list_after
    if check_ui:
        assert sorted(list_after) == sorted(app.contact.get_list())
