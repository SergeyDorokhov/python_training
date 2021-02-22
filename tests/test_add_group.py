# -*- coding: utf-8 -*-

from model.group import Group


def test_add_group(app):
    app.group.create(Group(name="111", header="222", comment="333"))


def test_add_empty_group(app):
    app.group.create(Group(name="", header="", comment=""))
