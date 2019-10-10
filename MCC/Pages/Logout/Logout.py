from selenium.webdriver.support.ui import Select

class LogoutPage():

    def __init__(self, driver):
        self.driver = driver
        self.logout_xpath = "//a[@class='logout']"


    def SignOut(self):
        self.driver.find_element_by_xpath(self.logout_xpath).click()


