from selenium import webdriver
import selenium

class LoginPage():

    def __init__(self, driver):
        self.driver = driver
        self.username_txtbx_name = "login"
        self.password_txtbx_name = "password"
        self.login_btn_id = "submit"

    def enter_username(self, username):
        self.driver.find_element_by_name(self.username_txtbx_name).clear()
        self.driver.find_element_by_name(self.username_txtbx_name).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element_by_name(self.password_txtbx_name).clear()
        self.driver.find_element_by_name(self.password_txtbx_name).send_keys(password)

    def click_loginbtn(self):
        self.driver.find_element_by_id(self.login_btn_id).click()
