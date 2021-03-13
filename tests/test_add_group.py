# -*- coding: utf-8 -*-

from model.group import Group


def test_add_group(app, json_groups):
    group = json_groups
    list_before = app.group.get_group_list()
    app.group.create(group)
    assert len(list_before) + 1 == app.group.count()
    list_after = app.group.get_group_list()
    list_before.append(group)
    assert sorted(list_before, key=Group.id_or_max) == sorted(list_after, key=Group.id_or_max)

# @pytest.mark.parametrize("group", testdata, ids=(repr(x) for x in testdata))
# def test_add_group(app, group):
#     list_before = app.group.get_group_list()
#     app.group.create(group)
#     assert len(list_before) + 1 == app.group.count()
#     list_after = app.group.get_group_list()
#     list_before.append(group)
#     assert sorted(list_before, key=Group.id_or_max) == sorted(list_after, key=Group.id_or_max)
