# -*- coding: utf-8 -*-

from model.group import Group


def test_add_group(app, db, json_groups, check_ui):
    group = json_groups
    list_before = db.get_group_list()
    app.group.create(group)
    list_after = db.get_group_list()
    list_before.append(group)
    assert sorted(list_before, key=Group.id_or_max) == sorted(list_after, key=Group.id_or_max)
    if check_ui:
        assert sorted(list_after, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
