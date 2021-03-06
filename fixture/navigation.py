class NavigationHelper:
    def __init__(self, app, base_url):
        self.app = app
        self.base_url = base_url

    def open_auth_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("addressbook/") and len(
                wd.find_elements_by_xpath("//input[@value='Login']")) > 0):
            wd.get(self.base_url)

    def open_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("addressbook/") and len(
                wd.find_elements_by_link_text("Number of results")) > 0):
            wd.find_element_by_link_text("home").click()

    def open_groups_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("group.php") and len(
                wd.find_elements_by_link_text("new")) > 1):
            wd.find_element_by_link_text("groups").click()
