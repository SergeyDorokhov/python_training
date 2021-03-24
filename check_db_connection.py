from fixture.orm import ORMFixture

db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

try:
    groups = db.get_contact_list()
    for group in groups:
        print(group)

finally:
    pass
