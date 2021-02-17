class GroupHelper:
    def __init__(self, app):
        self.app = app

    def create(self, group):
        wd = self.app.wd
        self.app.navigation.open_groups_page()
        wd.find_element_by_xpath("(//input[@name='new'])[2]").click()
        self.fill_group_form(group, wd)
        wd.find_element_by_name("submit").click()
        self.app.navigation.open_groups_page()

    def delete_first_group(self):
        wd = self.app.wd
        self.app.navigation.open_groups_page()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_name("delete").click()
        self.app.navigation.open_groups_page()

    def edit_first_group(self, group):
        wd = self.app.wd
        self.app.navigation.open_groups_page()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_name("edit").click()
        self.fill_group_form(group, wd)
        wd.find_element_by_name("update").click()
        self.app.navigation.open_groups_page()

    def fill_group_form(self, group, wd):
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.comment)
