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

    def get_contact_list_with_all_attribute(self):
        list_contacts = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname, home, mobile, work, email, email2, email3 from addressbook")
            for row in cursor:
                (id, firstname, lastname, home, mobile, work, email, email2, email3) = row
                list_contacts.append(Contact(id_contact=str(id), firstname=firstname, lastname=lastname,
                                             home_phone=home, mobile_phone=mobile, work_phone=work,
                                             email=email, email2=email2, email3=email3))
        finally:
            cursor.close()
        return list_contacts

    def get_contacts_from_group(self, group):
        list_contacts = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("""
            select a.id, a.firstname , a.lastname from addressbook a 
            join address_in_groups g 
            on a.id = g.id 
            where g.group_id = '%s'
            """ % group.id)
            for row in cursor:
                (id, firstname, lastname) = row
                list_contacts.append(Contact(id_contact=str(id), firstname=firstname, lastname=lastname))
        finally:
            cursor.close()
        return list_contacts

    def destroy(self):
        self.connection.close()

    def get_group_with_contacts(self):
        list_groups = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select distinct group_id from address_in_groups group by group_id")
            rows = cursor.fetchall()
            for row in rows:
                list_groups.append(Group(id=str(row[0])))
        finally:
            cursor.close()
        return list(list_groups)
