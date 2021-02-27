class Contact:
    def __init__(self, firstname=None, lastname=None, home_phone=None, id_contact=None):
        self.firstname = firstname
        self.lastname = lastname
        self.home_phone = home_phone
        self.id_contact = id_contact

    def __eq__(self, other):
        return self.id_contact == other.id_contact and self.firstname == other.firstname \
               and self.lastname == other.lastname

    def __lt__(self, other):
        return int(self.id_contact) < int(other.id_contact)

    def __repr__(self):
        return "%s %s: %s" % (self.lastname, self.firstname, self.id_contact)

    def get_id(self):
        return int(self.id_contact)
