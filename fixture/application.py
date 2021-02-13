from selenium import webdriver

from python_training.fixture.contact import ContactHelper
from python_training.fixture.group import GroupHelper
from python_training.fixture.session import SessionHelper


class Application:
    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    def open_auth_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def open_home_page(self):
        wd = self.wd
        wd.find_element_by_link_text("home").click()

    def destroy(self):
        self.wd.quit()
