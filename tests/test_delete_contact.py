# -*- coding: utf-8 -*-


def test_delete_first_contact(app):
    app.contact.create_if_not_exist()
    app.contact.delete_first_contact()
