from model.contact import Contact


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.app.navigation.open_home_page()
        self.contact_cache = None

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.app.navigation.open_home_page()
        self.contact_cache = None

    def edit_first_contact(self, contact):
        self.edit_contact_by_index(contact, 0)

    def edit_contact_by_index(self, contact, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()
        wd.find_elements_by_xpath("//img[@title='Edit']")[index].click()
        self.fill_contact_form(contact)
        wd.find_element_by_name("update").click()
        self.app.navigation.open_home_page()
        self.contact_cache = None

    def fill_contact_form(self, contact):
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("home", contact.home_phone)

    def change_field_value(self, field, value):
        wd = self.app.wd
        if value is not None:
            wd.find_element_by_name(field).click()
            wd.find_element_by_name(field).clear()
            wd.find_element_by_name(field).send_keys(value)

    def count(self):
        wd = self.app.wd
        self.app.navigation.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    def create_if_not_exist(self):
        if self.app.contact.count() == 0:
            self.app.contact.create(Contact(firstname="First contact"))

    contact_cache = None

    def get_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.contact_cache = []
            for entry in wd.find_elements_by_name("entry"):
                id_entry = entry.find_element_by_name("selected[]").get_attribute("value")
                last_name = entry.find_element_by_xpath("td[2]").text
                first_name = entry.find_element_by_xpath("td[3]").text
                self.contact_cache.append(Contact(firstname=first_name,
                                                  lastname=last_name, id_contact=id_entry))
        return self.contact_cache

    def get_next_id(self, contacts):
        # max_id = sorted(contacts, key=lambda contact: int(contact.id_contact))[-1].id_contact
        max_id = sorted(contacts, key=Contact.get_id)[-1].id_contact
        return str(int(max_id) + 1)
