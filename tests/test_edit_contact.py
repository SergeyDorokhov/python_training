# -*- coding: utf-8 -*-
from random import randrange

from model.contact import Contact


def test_edit_first_contact(app):
    app.contact.create_if_not_exist()
    list_before = app.contact.get_list()
    contact = Contact(firstname="new firstname", lastname="new lastname", home_phone=123,
                      mobile_phone=456, work_phone=789)
    contact.id_contact = list_before[0].id_contact
    app.contact.edit_first_contact(contact)
    assert len(list_before) == app.contact.count()
    list_before[0] = contact
    list_after = app.contact.get_list()
    assert sorted(list_before) == sorted(list_after)


def test_edit_some_contact(app):
    app.contact.create_if_not_exist()
    list_before = app.contact.get_list()
    index = randrange(len(list_before))
    contact = Contact(firstname="new firstname", lastname="new lastname", home_phone=123,
                      mobile_phone=456, work_phone=789)
    contact.id_contact = list_before[index].id_contact
    app.contact.edit_contact_by_index(contact, index)
    assert len(list_before) == app.contact.count()
    list_before[index] = contact
    list_after = app.contact.get_list()
    assert sorted(list_before) == sorted(list_after)
