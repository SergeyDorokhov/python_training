from model.group import Group


def test_edit_first_group_name(app):
    app.group.create_if_not_exist()
    app.group.edit_first_group(Group(name="new name"))


def test_edit_first_group_header(app):
    app.group.create_if_not_exist()
    app.group.edit_first_group(Group(header="new header"))
