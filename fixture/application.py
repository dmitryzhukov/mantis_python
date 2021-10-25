from model.credentials import Credentials
from selenium import webdriver

from fixture.project import ProjectHelper
from fixture.session import SessionHelper
from fixture.soap import SoapHelper


class Application:
    def __init__(self, browser, base_url, credentials: Credentials, soap_url):
        if browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        self.wd.implicitly_wait(1)
        self.session = SessionHelper(self)
        self.project = ProjectHelper(self)
        self.soap = SoapHelper(self)
        self.base_url = base_url
        self.credentials = credentials
        self.soap_url = soap_url

    def open_home_page(self):
        wd = self.wd
        if not (wd.current_url.endswith("/addressbook/")):
            wd.get(self.base_url)

    def change_field_value(self, field_name, text):
        wd = self.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def destroy(self):
        self.wd.quit()

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False
