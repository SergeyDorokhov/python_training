import random

from model.group import Group


def test_edit_some_group_name(app, db, check_ui):
    app.group.create_if_not_exist()
    list_before = db.get_group_list()
    group = Group(name="new name")
    edit_group = random.choice(list_before)
    group.id = edit_group.id
    app.group.edit_some_group_by_id(group, group.id)
    list_after = db.get_group_list()
    assert len(list_before) == len(list_after)
    list_before.remove(edit_group)
    list_before.append(group)
    assert sorted(list_before, key=Group.id_or_max) == sorted(list_after, key=Group.id_or_max)
    if check_ui:
        assert sorted(list_after, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
