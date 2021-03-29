import random

from model.group import Group


def test_add_contact_in_group(app, db, check_ui):
    # Проверим, что есть группы и контакты
    groups = db.get_group_list()
    if len(groups) == 0:
        app.group.create_if_not_exist()
    contacts = db.get_contact_list()
    if len(contacts) == 0:
        app.contact.create_if_not_exist()
    free_contacts = db.get_contacts_free_of_group()
    groups_before = []
    # Если нет контакта без группы, создадим новую группу и положим в нее случайный контакт
    if len(free_contacts) == 0:
        app.group.create(Group("Empty group %s" % random.randint(0, 1000)))
        group = db.get_group_list()[-1]
        free_contact = random.choice(db.get_contact_list())
        groups_before = db.get_groups_from_contact(free_contact)
        app.contact.add_contact_to_group_by_id(group, free_contact)
    # Если есть контакты без группы, положим любой из них в случайную группу
    else:
        free_contact = random.choice(free_contacts)
        group = random.choice(db.get_group_list())
        app.contact.add_contact_to_group_by_id(group, free_contact)
    groups_after = db.get_groups_from_contact(free_contact)
    groups_before.append(group)
    assert groups_before == groups_after
