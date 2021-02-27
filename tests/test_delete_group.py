from random import randrange


def test_delete_first_group(app):
    app.group.create_if_not_exist()
    list_before = app.group.get_group_list()
    app.group.delete_first_group()
    assert len(list_before) - 1 == app.group.count()
    list_after = app.group.get_group_list()
    list_before[0:1] = []
    assert list_before == list_after


def test_delete_some_group(app):
    app.group.create_if_not_exist()
    list_before = app.group.get_group_list()
    index = randrange(len(list_before))
    app.group.delete_group_by_index(index)
    assert len(list_before) - 1 == app.group.count()
    list_after = app.group.get_group_list()
    list_before[index: index + 1] = []
    assert list_before == list_after
