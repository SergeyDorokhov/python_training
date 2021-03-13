import getopt
import os
import random
import re
import string
import sys

import jsonpickle

from model.group import Group

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups, file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 4
f = "data/groups.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " " * 20
    rand_string = (prefix + " ".join([random.choice(symbols) for x in range(random.randrange(maxlen))]))
    return re.sub(r'\s+', ' ', rand_string)


testdata = [Group(name="", header="", comment="")] + [
    Group(name=random_string("name", 10).rstrip(), header=random_string("header", 15),
          comment=random_string("comment", 30)) for
    i in range(n)]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)
with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
