class GroupHelper:
    def __init__(self, app):
        self.app = app

    def create(self, group):
        wd = self.app.wd
        self.app.navigation.open_groups_page()
        wd.find_element_by_xpath("(//input[@name='new'])[2]").click()
        self.fill_group_form(group)
        wd.find_element_by_name("submit").click()
        self.app.navigation.open_home_page()

    def delete_first_group(self):
        wd = self.app.wd
        self.app.navigation.open_groups_page()
        self.select_first_group()
        wd.find_element_by_name("delete").click()
        self.app.navigation.open_home_page()

    def edit_first_group(self, group):
        wd = self.app.wd
        self.app.navigation.open_groups_page()
        self.select_first_group()
        wd.find_element_by_name("edit").click()
        self.fill_group_form(group)
        wd.find_element_by_name("update").click()
        self.app.navigation.open_home_page()

    def fill_group_form(self, group):
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.comment)

    def change_field_value(self, field_name, value):
        wd = self.app.wd
        if value is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(value)

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()
