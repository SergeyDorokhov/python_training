# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    list_before = app.group.get_group_list()
    group = Group(name="111", header="222", comment="333")
    app.group.create(group)
    list_after = app.group.get_group_list()
    assert len(list_before) + 1 == len(list_after)
    list_before.append(group)
    assert sorted(list_before, key=Group.id_or_max) == sorted(list_after, key=Group.id_or_max)


def test_add_group_with_logout(app):
    list_before = app.group.get_group_list()
    group = Group(name="111", header="222", comment="333")
    app.group.create(group)
    list_after = app.group.get_group_list()
    app.session.logout()
    assert len(list_before) + 1 == len(list_after)
    list_before.append(group)
    assert sorted(list_before, key=Group.id_or_max) == sorted(list_after, key=Group.id_or_max)


def test_add_empty_group(app):
    list_before = app.group.get_group_list()
    group = Group(name="", header="", comment="")
    app.group.create(group)
    list_after = app.group.get_group_list()
    assert len(list_before) + 1 == len(list_after)
    list_before.append(group)
    assert sorted(list_before, key=Group.id_or_max) == sorted(list_after, key=Group.id_or_max)
