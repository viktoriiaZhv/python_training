# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import unittest
from contact import Contact
from extras import Extras

class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def test_untitled_test_case(self):
        wd = self.wd
        Extras.open_home_page(wd)
        Extras.login(wd, "admin", "secret")
        self.add_new_contact(wd, Contact("maria","nikolavna","zhistovskaya","hello world",
                        "sber","kazahstan, atarbekova 6","35358800",
                        "vistoskaya@gmail.com","1997","2020","njklnlk","test for recorder"))
        self.return_contact_page(wd)
        Extras.logout(wd)

    @staticmethod
    def return_contact_page(wd):
        # return to home page
        wd.find_element("link text", "home page").click()
        wd.find_element("id", "top").click()

    @staticmethod
    def add_new_contact(wd, contact):
        # init contact creation
        wd.find_element("link text", "add new").click()
        # fill contact form
        wd.find_element("name", "firstname").click()
        wd.find_element("name", "firstname").clear()
        wd.find_element("name", "firstname").send_keys(contact.firstname)
        wd.find_element("name", "middlename").click()
        wd.find_element("name", "middlename").clear()
        wd.find_element("name", "middlename").send_keys(contact.middlename)
        wd.find_element("name", "lastname").click()
        wd.find_element("name", "lastname").clear()
        wd.find_element("name", "lastname").send_keys(contact.lastname)
        wd.find_element("name", "title").click()
        wd.find_element("name", "title").clear()
        wd.find_element("name", "title").send_keys(contact.title)
        wd.find_element("name", "company").click()
        wd.find_element("name", "company").clear()
        wd.find_element("name", "company").send_keys(contact.company)
        wd.find_element("name", "address").click()
        wd.find_element("name", "address").click()
        wd.find_element("name", "address").clear()
        wd.find_element("name", "address").send_keys(contact.address)
        wd.find_element("name", "mobile").click()
        wd.find_element("name", "mobile").clear()
        wd.find_element("name", "mobile").send_keys(contact.mobile)
        wd.find_element("name", "work").click()
        wd.find_element("name", "email").click()
        wd.find_element("name", "email").clear()
        wd.find_element("name", "email").send_keys(contact.email)
        wd.find_element("name", "bday").click()
        Select(wd.find_element("name", "bday")).select_by_visible_text("13")
        wd.find_element("xpath", "//option[@value='13']").click()
        wd.find_element("name", "bmonth").click()
        Select(wd.find_element("name", "bmonth")).select_by_visible_text("August")
        wd.find_element("xpath", "//option[@value='August']").click()
        wd.find_element("name", "byear").click()
        wd.find_element("name", "byear").clear()
        wd.find_element("name", "byear").send_keys(contact.byear)
        wd.find_element("name", "aday").click()
        Select(wd.find_element("name", "aday")).select_by_visible_text("20")
        wd.find_element("xpath", "//div[@id='content']/form/select[3]/option[22]").click()
        wd.find_element("name", "amonth").click()
        Select(wd.find_element("name", "amonth")).select_by_visible_text("December")
        wd.find_element("xpath", "//div[@id='content']/form/select[4]/option[13]").click()
        wd.find_element("name", "ayear").click()
        wd.find_element("name", "ayear").clear()
        wd.find_element("name", "ayear").send_keys(contact.ayear)
        wd.find_element("name", "new_group").click()
        Select(wd.find_element("name", "new_group")).select_by_visible_text("vikaTest")
        wd.find_element("xpath", "//div[@id='content']/form/select[5]/option[11]").click()
        wd.find_element("name", "address2").click()
        wd.find_element("name", "address2").clear()
        wd.find_element("name", "address2").send_keys(contact.address2)
        wd.find_element("name", "notes").click()
        wd.find_element("name", "notes").clear()
        wd.find_element("name", "notes").send_keys(contact.notes)
        wd.find_element("xpath", "//input[21]").click()

    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()
