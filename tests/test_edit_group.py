from model.group import Group


def test_edit_first_group_name(app):
    app.group.create_if_not_exist()
    list_before = app.group.get_group_list()
    group = Group(name="new name")
    group.id = list_before[0].id
    app.group.edit_first_group(group)
    list_after = app.group.get_group_list()
    assert len(list_before) == len(list_after)
    list_before[0] = group
    assert sorted(list_before, key=Group.id_or_max) == sorted(list_after, key=Group.id_or_max)


def test_edit_first_group_header(app):
    app.group.create_if_not_exist()
    list_before = app.group.get_group_list()
    group = Group(name="new name")
    group.id = list_before[0].id
    app.group.edit_first_group(group)
    list_after = app.group.get_group_list()
    assert len(list_before) == len(list_after)
    list_before[0] = group
    assert sorted(list_before, key=Group.id_or_max) == sorted(list_after, key=Group.id_or_max)
