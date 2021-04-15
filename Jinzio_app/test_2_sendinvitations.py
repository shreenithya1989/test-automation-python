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
        self.driver.get(TestCaseConfig.APPLICATION_URL)
        self.is_element_present(TestCaseConfig.LOGIN_FIELD_LOCATOR)
        self.driver.maximize_window()

    def step1(self):
        # Click Login
        self.driver.find_element_by_id(TestCaseConfig.LOGIN_BUTTON_ID).click()

        # Enter Username
        elem = self.driver.find_element_by_id(TestCaseConfig.EMAIL_FIELD_ID)
        elem.clear()
        elem.send_keys("robotuser1@mailinator.com")

        # Enter Password
        elem = self.driver.find_element_by_id(TestCaseConfig.PASSWORD_FIELD_ID)
        elem.clear()
        elem.send_keys("*******")

        # Click Continue
        elem = self.driver.find_element_by_name("action")
        elem.click()

        WebDriverWait(self.driver, 10).until(EC.url_matches("https://app.jinzio.com/app/jobs/open"))
        self.assertIn("Recruitment Patform", self.driver.title)

    def step2(self):
        # Click My Profile

        self.is_element_present(TestCaseConfig.MY_PROFILE_LOCATOR)
        elem = self.driver.find_element_by_id("profile").click()
        WebDriverWait(self.driver, 10).until(EC.url_matches("https://app.jinzio.com/app/profile"))
        self.assertIn("Recruitment Patform", self.driver.title)

        # Click Invitations Tab

        self.is_element_present(TestCaseConfig.INVITATIONS_LOCATOR)
        elem = self.driver.find_element_by_id("rec-invitations").click()

        # Invite Recruiter Button

        self.is_element_present((By.ID, "recruiter-invitation-button"))
        elem = self.driver.find_element_by_id("recruiter-invitation-button").click()

        # Enter First,Lastname and Email
        elem = self.driver.find_element_by_id("rec-invitationlist-firstname")
        elem.clear()
        elem.send_keys("Jinzio")

        elem = self.driver.find_element_by_id("rec-invitationlist-lastname")
        elem.clear()
        elem.send_keys("REC" + TestCaseConfig.CUR_DATE)

        elem = self.driver.find_element_by_id("rec-invitationlist-email")
        elem.clear()
        print(TestCaseConfig.CUR_DATE)
        elem.send_keys("jinzio.rec" + TestCaseConfig.CUR_DATE + "@mailinator.com")

        # Click Send Invitation Button
        self.is_element_present((By.ID, "rec-sendinvitation-button"))
        elem = self.driver.find_element_by_id("rec-sendinvitation-button").click()
        self.driver.quit()

    def test_import_data(self):
        try:
            # Login to Application
            self.step1()

            # Send Invitations
            self.step2()

        except WebDriverException as ex:
            allure.attach(self.driver.get_screenshot_as_png(), name="Launch Screen",
                          attachment_type=AttachmentType.PNG)
            raise ex
