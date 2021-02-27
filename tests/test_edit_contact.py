# -*- coding: utf-8 -*-
from model.contact import Contact


def test_edit_first_contact(app):
    app.contact.create_if_not_exist()
    list_before = app.contact.get_list()
    contact = Contact(firstname="new firstname", lastname="new lastname", home_phone=0)
    contact.id_contact = list_before[0].id_contact
    app.contact.edit_first_contact(contact)
    list_after = app.contact.get_list()
    assert len(list_before) == len(list_after)
    assert sorted(list_before) == sorted(list_after)
