def test_delete_first_group(app):
    app.group.create_if_not_exist()
    list_before = app.group.get_group_list()
    app.group.delete_first_group()
    assert len(list_before) - 1 == app.group.count()
    list_after = app.group.get_group_list()
    list_before[0:1] = []
    assert list_before == list_after
