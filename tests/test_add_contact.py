# -*- coding: utf-8 -*-
import pytest

from python_training.fixture.application import Application
from python_training.model.contact import Contact


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.create_contact(Contact(firstname="AAA", lastname="BBB", home_phone="123456789"))
    app.session.logout()
