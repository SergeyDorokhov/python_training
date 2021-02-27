from random import randrange

from model.group import Group


def test_edit_first_group_name(app):
    app.group.create_if_not_exist()
    list_before = app.group.get_group_list()
    group = Group(name="new name")
    group.id = list_before[0].id
    app.group.edit_first_group(group)
    assert len(list_before) == app.group.count()
    list_after = app.group.get_group_list()
    list_before[0] = group
    assert sorted(list_before, key=Group.id_or_max) == sorted(list_after, key=Group.id_or_max)


def test_edit_first_group_header(app):
    app.group.create_if_not_exist()
    list_before = app.group.get_group_list()
    group = Group(name="new name")
    group.id = list_before[0].id
    app.group.edit_first_group(group)
    assert len(list_before) == app.group.count()
    list_after = app.group.get_group_list()
    list_before[0] = group
    assert sorted(list_before, key=Group.id_or_max) == sorted(list_after, key=Group.id_or_max)


def test_edit_some_group_name(app):
    app.group.create_if_not_exist()
    list_before = app.group.get_group_list()
    group = Group(name="new name")
    index = randrange(len(list_before))
    group.id = list_before[index].id
    app.group.edit_some_group(group, index)
    assert len(list_before) == app.group.count()
    list_after = app.group.get_group_list()
    list_before[index] = group
    assert sorted(list_before, key=Group.id_or_max) == sorted(list_after, key=Group.id_or_max)
