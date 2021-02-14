# -*- coding: utf-8 -*-

from model.contact import Contact


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="AAA", lastname="BBB", home_phone="123456789"))
    app.session.logout()
