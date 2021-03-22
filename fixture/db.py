import pymysql.cursors

from model.contact import Contact
from model.group import Group


class DbFixture:
    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)

    def get_group_list(self):
        list_groups = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list_groups.append(Group(id=str(id), name=name, header=header, comment=footer))
        finally:
            cursor.close()
        return list_groups

    def get_contact_list(self):
        list_contacts = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname from addressbook")
            for row in cursor:
                (id, firstname, lastname) = row
                list_contacts.append(Contact(id_contact=str(id), firstname=firstname, lastname=lastname))
        finally:
            cursor.close()
        return list_contacts

    def destroy(self):
        self.connection.close()
