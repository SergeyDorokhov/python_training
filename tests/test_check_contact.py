import re


def test_check_contacts_on_ui_with_db(app, db):
    contacts_from_ui = app.contact.get_list()
    contacts_from_db = db.get_contact_list_with_all_attribute()
    assert len(contacts_from_db) == len(contacts_from_ui)
    contacts_db_sort = sorted(contacts_from_db)
    contacts_ui_sort = sorted(contacts_from_ui)
    assert contacts_db_sort == contacts_ui_sort

    for i in range(len(contacts_from_db)):
        assert merge_emails_like_on_home_page(contacts_db_sort[i]) == contacts_ui_sort[i].all_emails_on_home_page
        assert merge_phones_like_on_home_page(contacts_db_sort[i]) == contacts_ui_sort[i].all_phones_from_home_page


def test_check_contact_on_home_page(app):
    contact_from_home_page = app.contact.get_list()[0]
    contact_from_edit_page = app.contact.get_contact_from_edit_page(0)
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.all_phones_from_home_page == \
           merge_phones_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_emails_on_home_page == \
           merge_emails_like_on_home_page(contact_from_edit_page)


def clear(string):
    return re.sub("[() -]", "", string)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "", map(lambda x: clear(x), filter(lambda x: x is not None,
                                                                              [contact.home_phone, contact.mobile_phone,
                                                                               contact.work_phone]))))


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "", map(lambda x: clear(x), filter(lambda x: x is not None,
                                                                              [contact.email, contact.email2,
                                                                               contact.email3]))))
