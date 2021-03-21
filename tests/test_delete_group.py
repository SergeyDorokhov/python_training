import random

from model.group import Group


def test_delete_some_group(app, db, check_ui):
    app.group.create_if_not_exist()
    list_before = db.get_group_list()
    group = random.choice(list_before)
    app.group.delete_group_by_id(group.id)
    assert len(list_before) - 1 == app.group.count()
    list_after = db.get_group_list()
    list_before.remove(group)
    assert list_before == list_after
    if check_ui:
        assert sorted(list_after, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
