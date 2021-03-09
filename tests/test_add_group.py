# -*- coding: utf-8 -*-
import random
import re
import string

import pytest

from model.group import Group


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " " * 20
    rand_string = (prefix + " ".join([random.choice(symbols) for x in range(random.randrange(maxlen))]))
    return re.sub(r'\s+', ' ', rand_string)


testdata = [Group(name="", header="", comment="")] + [
    Group(name=random_string("name", 10).rstrip(), header=random_string("header", 15),
          comment=random_string("comment", 30)) for
    i in range(5)]


@pytest.mark.parametrize("group", testdata, ids=(repr(x) for x in testdata))
def test_add_group(app, group):
    list_before = app.group.get_group_list()
    app.group.create(group)
    assert len(list_before) + 1 == app.group.count()
    list_after = app.group.get_group_list()
    list_before.append(group)
    assert sorted(list_before, key=Group.id_or_max) == sorted(list_after, key=Group.id_or_max)
