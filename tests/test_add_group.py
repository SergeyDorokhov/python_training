# -*- coding: utf-8 -*-
import allure

from model.group import Group


def test_add_group(app, db, json_groups, check_ui):
    group = json_groups
    with allure.step('Given a group list'):
        list_before = db.get_group_list()
    with allure.step('When i add a group %s to the list' % group):
        app.group.create(group)
    with allure.step('Then a new group list is equal the old list with added group'):
        list_after = db.get_group_list()
        list_before.append(group)
        assert sorted(list_before, key=Group.id_or_max) == sorted(list_after, key=Group.id_or_max)
        if check_ui:
            assert sorted(list_after, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
