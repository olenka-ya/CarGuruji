from selenium.webdriver.support.ui import Select

class LoginPage():

    def __init__(self, driver):
        self.driver = driver
        self.email_address = "//input[@id='email']"
        self.password = "//input[@id='passwd']"
        self.signin_button = "//form[@id='login_form']//span[1]"

    def SignIn(self,email,passw):
        self.driver.find_element_by_xpath(self.email_address).send_keys(email)
        self.driver.find_element_by_xpath(self.password).send_keys(passw)
        self.driver.find_element_by_xpath(self.signin_button).click()

