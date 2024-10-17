# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest
from group import Group
from extras import Extras


class TestAddGroup(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def test_add_group(self):
        wd = self.wd
        Extras.open_home_page(wd)
        Extras.login(wd, "admin", "secret")
        self.create_group(wd, Group("my first success", "new header", "new footer"))
        self.return_to_groups_page(wd)
        Extras.logout(wd)

    def test_empty_group(self):
        wd = self.wd
        Extras.open_home_page(wd)
        Extras.login(wd, "admin", "secret")
        self.create_group(wd, Group("", "", ""))
        self.return_to_groups_page(wd)
        Extras.logout(wd)

    @staticmethod
    def return_to_groups_page(wd):
        wd.find_element("link text", "group page").click()

    @staticmethod
    def create_group(wd, group):
        # init group creation
        wd.find_element("name", "new").click()
        wd.find_element("id", "content").click()
        # fill group form
        wd.find_element("name", "group_name").click()
        wd.find_element("name", "group_name").clear()
        wd.find_element("name", "group_name").send_keys(group.name)
        wd.find_element("name", "group_header").click()
        wd.find_element("name", "group_header").clear()
        wd.find_element("name", "group_header").send_keys(group.header)
        wd.find_element("name", "group_footer").click()
        wd.find_element("name", "group_footer").clear()
        wd.find_element("name", "group_footer").send_keys(group.footer)
        # submit group creation
        wd.find_element("name", "submit").click()

    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()
