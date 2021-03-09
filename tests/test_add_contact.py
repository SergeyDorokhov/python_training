# -*- coding: utf-8 -*-

from model.contact import Contact


def test_add_contact(app):
    list_before = app.contact.get_list()
    contact = Contact(firstname="AAA", lastname="BBB", id_contact=app.contact.get_next_id(list_before),
                      home_phone="123456789", work_phone="456", mobile_phone="789")
    app.contact.create(contact)
    assert len(list_before) + 1 == app.contact.count()
    list_after = app.contact.get_list()
    list_before.append(contact)
    assert sorted(list_before) == sorted(list_after)
