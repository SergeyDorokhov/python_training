# -*- coding: utf-8 -*-
import random
import re
import string

import pytest

from model.contact import Contact


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " " * 5
    rand_string = (prefix + " ".join([random.choice(symbols) for x in range(random.randrange(maxlen))]))
    return re.sub(r'\s+', ' ', rand_string)


def random_numbers(maxlen):
    symbols = string.digits
    rand_num = ("".join([random.choice(symbols) for x in range(random.randrange(maxlen))]))
    return rand_num


testdata = [
    Contact(firstname=random_string("firstname: ", 10).rstrip(), lastname=random_string("lastname: ", 8).rstrip(),
            home_phone=random_numbers(10), work_phone=random_numbers(10),
            mobile_phone=random_numbers(7)) for
    i in range(3)]


@pytest.mark.parametrize("contact", testdata, ids=(repr(x) for x in testdata))
def test_add_contact(app, contact):
    list_before = app.contact.get_list()
    contact.id_contact = app.contact.get_next_id(list_before)
    app.contact.create(contact)
    assert len(list_before) + 1 == app.contact.count()
    list_after = app.contact.get_list()
    list_before.append(contact)
    assert sorted(list_before) == sorted(list_after)
