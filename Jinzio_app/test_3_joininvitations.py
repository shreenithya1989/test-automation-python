import unittest

import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException
from Jinzio_app.config import TestCaseConfig


class JinzioAppTest(unittest.TestCase):
    def is_element_present(self, locator):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(TestCaseConfig.JOIN_URL)
        self.is_element_present((By.ID, "email"))
        self.driver.maximize_window()

    def step1(self):

        # Enter Email
        elem = self.driver.find_element_by_id("email")
        elem.clear()
        elem.send_keys("jinzio.rec" + TestCaseConfig.CUR_DATE + "@mailinator.com")

        # Enter Password
        elem = self.driver.find_element_by_id("password")
        elem.clear()
        elem.send_keys("Test@123")

        # Click Continue
        elem = self.driver.find_element_by_name("action")
        elem.click()

        WebDriverWait(self.driver, 10).until(EC.url_matches("https://app.jinzio.com/app/task/status/open"))
        self.assertIn("Recruitment Patform", self.driver.title)
        self.driver.quit()

    def test_import_data(self):
        try:
            # Accept Invitation
            self.step1()



        except WebDriverException as ex:
            allure.attach(self.driver.get_screenshot_as_png(), name="Launch Screen",
                          attachment_type=AttachmentType.PNG)
            raise ex
