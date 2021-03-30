import random


def test_delete_contact_from_group(app, db, check_ui):
    groups_with_contact = db.get_group_with_contacts()
    # Если есть группы с контактами
    if len(groups_with_contact) != 0:
        group_with_contact = random.choice(groups_with_contact)
        contact = random.choice(db.get_contacts_from_group(group_with_contact))
        groups_before = db.get_groups_from_contact(contact)
        app.contact.delete_contact_from_group(contact.id_contact, group_with_contact)
        groups_after = db.get_groups_from_contact(contact)
        groups_before.remove(group_with_contact)
        assert groups_before == groups_after
    # Если нет группы с контактами (и в частности нет групп или контактов)
    else:
        groups = db.get_group_list()
        if len(groups) == 0:
            app.group.create_if_not_exist()
        contacts = db.get_contact_list()
        if len(contacts) == 0:
            app.contact.create_if_not_exist()
        free_contact = random.choice(db.get_contacts_free_of_group())
        group = random.choice(db.get_group_list())
        app.contact.add_contact_to_group_by_id(group, free_contact)
        groups_before = db.get_groups_from_contact(free_contact)
        app.contact.delete_contact_from_group(free_contact.id_contact, group)
        groups_after = db.get_groups_from_contact(free_contact)
        groups_before.remove(group)
        assert groups_before == groups_after
