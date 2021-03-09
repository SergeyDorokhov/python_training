class Contact:
    def __init__(self, firstname=None, lastname=None, id_contact=None, mobile_phone=None, home_phone=None,
                 work_phone=None, all_phones_from_home_page=None):
        self.firstname = firstname
        self.lastname = lastname
        self.mobile_phone = mobile_phone
        self.home_phone = home_phone
        self.work_phone = work_phone
        self.id_contact = id_contact
        self.all_phones_from_home_page = all_phones_from_home_page

    def __eq__(self, other):
        return self.id_contact == other.id_contact and self.firstname == other.firstname \
               and self.lastname == other.lastname

    def __lt__(self, other):
        return int(self.id_contact) < int(other.id_contact)

    def __repr__(self):
        return "%s %s: %s" % (self.lastname, self.firstname, self.id_contact)

    def get_id(self):
        return int(self.id_contact)
