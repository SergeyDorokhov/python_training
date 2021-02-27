# -*- coding: utf-8 -*-


def test_delete_first_contact(app):
    app.contact.create_if_not_exist()
    list_before = app.contact.get_list()
    app.contact.delete_first_contact()
    assert len(list_before) - 1 == app.contact.count()
    list_after = app.contact.get_list()
    list_before[0:1] = []
    assert list_before == list_after
