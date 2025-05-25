from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR,"#login_link")

class LoginPageLocators():
    REGISTRATION_EMAIL_LINK = (By.CSS_SELECTOR,"#id_registration-email")
    REGISTRATION_PASSWORD_LINK = (By.CSS_SELECTOR,"#id_registration-password1")
    REGISTRATION_CONFIRM_PASSWORD_LINK = (By.CSS_SELECTOR,"#id_registration-password2")
    REGISTRATION_FORM_BUTTON = (By.XPATH,"//*[@value='Register']")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    LOGIN_EMAIL_LINK = (By.CSS_SELECTOR,"#id_login-username")
    LOGIN_PASSWORD_LINK = (By.CSS_SELECTOR,"#id_login-password")
    LOGIN_FORM_BUTTON = (By.XPATH,"//*[@value='Log In']")
