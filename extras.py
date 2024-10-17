class Extras:
    @staticmethod
    def login(wd, username, password):
        wd.find_element("name", "user").click()
        wd.find_element("name", "user").clear()
        wd.find_element("name", "user").send_keys(username)
        wd.find_element("xpath", "//label[2]").click()
        wd.find_element("name", "pass").click()
        wd.find_element("name", "pass").clear()
        wd.find_element("name", "pass").send_keys(password)
        wd.find_element("xpath", "//input[@value='Login']").click()

    @staticmethod
    def open_home_page(wd):
        wd.get("http://localhost/addressbook/group.php")

    @staticmethod
    def logout(wd):
        wd.find_element("link text", "Logout").click()