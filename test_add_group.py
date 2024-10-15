# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest

class TestAddGroup(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def test_add_group(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, "admin", "secret")
        self.create_group(wd, "my first success", "new header", "new footer")
        self.return_to_groups_page(wd)
        self.logout(wd)

    def test_empty_group(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, "admin", "secret")
        self.create_group(wd, "", "", "")
        self.return_to_groups_page(wd)
        self.logout(wd)

    def logout(self, wd):
        wd.find_element("link text", "Logout").click()

    def return_to_groups_page(self, wd):
        wd.find_element("link text", "group page").click()

    def create_group(self, wd, name, header, footer):
        # init group creation
        wd.find_element("name", "new").click()
        wd.find_element("id", "content").click()
        # fill group form
        wd.find_element("name", "group_name").click()
        wd.find_element("name", "group_name").clear()
        wd.find_element("name", "group_name").send_keys(name)
        wd.find_element("name", "group_header").click()
        wd.find_element("name", "group_header").clear()
        wd.find_element("name", "group_header").send_keys(header)
        wd.find_element("name", "group_footer").click()
        wd.find_element("name", "group_footer").clear()
        wd.find_element("name", "group_footer").send_keys(footer)
        # submit group creation
        wd.find_element("name", "submit").click()

    def login(self, wd, username, password):
        wd.find_element("name", "user").click()
        wd.find_element("name", "user").clear()
        wd.find_element("name", "user").send_keys(username)
        wd.find_element("xpath", "//label[2]").click()
        wd.find_element("name", "pass").click()
        wd.find_element("name", "pass").clear()
        wd.find_element("name", "pass").send_keys(password)
        wd.find_element("xpath", "//input[@value='Login']").click()

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/group.php")

    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()
