def test_delete_first_group(app):
    app.group.create_if_not_exist()
    app.group.delete_first_group()
