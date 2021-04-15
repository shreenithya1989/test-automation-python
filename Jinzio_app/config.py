from selenium.webdriver.common.by import By
from datetime import date

today = date.today()


class TestCaseConfig:
    APPLICATION_URL = "https://app.jinzio.com/auth/login"
    JOIN_URL = "https://app.jinzio.com/join"

    EMAIL_FIELD_ID = "username"
    EMAIL_FIELD_LOCATOR = (By.ID, EMAIL_FIELD_ID)

    PASSWORD_FIELD_ID = "password"
    PASSWORD_FIELD_LOCATOR = (By.ID, PASSWORD_FIELD_ID)

    LOGIN_BUTTON_ID = "loginButton"
    LOGIN_FIELD_LOCATOR = (By.ID, LOGIN_BUTTON_ID)

    MY_PROFILE_ID = "profile"
    MY_PROFILE_LOCATOR = (By.ID, MY_PROFILE_ID)

    INVITATIONS_ID = "rec-invitations"
    INVITATIONS_LOCATOR = (By.ID, INVITATIONS_ID)

    CUR_DATE = today.strftime("%d-%m-%Y")
