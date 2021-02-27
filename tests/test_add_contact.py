# -*- coding: utf-8 -*-

from model.contact import Contact


def test_add_contact(app):
    list_before = app.contact.get_list()
    contact = Contact(firstname="AAA", lastname="BBB", home_phone="123456789",
                      id_contact=app.contact.get_next_id(list_before))
    app.contact.create(contact)
    list_after = app.contact.get_list()
    assert len(list_before) + 1 == len(list_after)
    list_before.append(contact)
    assert sorted(list_before) == sorted(list_after)
