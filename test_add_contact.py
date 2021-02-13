# -*- coding: utf-8 -*-
import pytest

from application import Application
from contact import Contact


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.login(username="admin", password="secret")
    app.create_contact(Contact(firstname="AAA", lastname="BBB", home_phone="123456789"))
    app.logout()
