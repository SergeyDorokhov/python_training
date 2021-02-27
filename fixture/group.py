from model.group import Group


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
        self.group_cache = None

    def delete_first_group(self):
        self.delete_group_by_index(0)

    def delete_group_by_index(self, index):
        wd = self.app.wd
        self.app.navigation.open_groups_page()
        self.select_group_by_index(index)
        wd.find_element_by_name("delete").click()
        self.app.navigation.open_home_page()
        self.group_cache = None

    def edit_first_group(self, group):
        self.edit_some_group(group, 0)

    def edit_some_group(self, group, index):
        wd = self.app.wd
        self.app.navigation.open_groups_page()
        self.select_group_by_index(index)
        wd.find_element_by_name("edit").click()
        self.fill_group_form(group)
        wd.find_element_by_name("update").click()
        self.app.navigation.open_home_page()
        self.group_cache = None

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
        self.select_group_by_index(0)

    def select_group_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def count(self):
        wd = self.app.wd
        self.app.navigation.open_groups_page()
        return len(wd.find_elements_by_name("selected[]"))

    def create_if_not_exist(self):
        if self.app.group.count() == 0:
            self.app.group.create(Group("First group"))

    group_cache = None

    def get_group_list(self):
        if self.group_cache is None:
            wd = self.app.wd
            self.app.navigation.open_groups_page()
            self.group_cache = []
            for group in wd.find_elements_by_css_selector("span.group"):
                name = group.text
                id = group.find_element_by_name("selected[]").get_attribute("value")
                self.group_cache.append(Group(name=name, id=id))
        return self.group_cache
