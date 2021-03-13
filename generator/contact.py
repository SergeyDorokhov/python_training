import getopt
import os
import random
import re
import string
import sys

import jsonpickle
import pytest

from model.contact import Contact

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts, file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 4
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " " * 5
    rand_string = (prefix + "".join([random.choice(symbols) for _ in range(random.randrange(maxlen))]))
    return re.sub(r'\s+', ' ', rand_string)


def random_numbers(maxlen):
    symbols = string.digits
    rand_num = "1" + ("".join([random.choice(symbols) for _ in range(random.randrange(maxlen))]))
    return rand_num


testdata = [
    Contact(firstname=random_string("firstname: ", 10).rstrip(), lastname=random_string("lastname: ", 8).rstrip(),
            home_phone=random_numbers(10), work_phone=random_numbers(10),
            mobile_phone=random_numbers(7)) for
    i in range(n)]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)
with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))