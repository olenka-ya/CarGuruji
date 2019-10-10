from selenium import webdriver
from selenium.webdriver.support.ui import Select

class addtocartPage():

    def __init__(self, driver):
        self.driver = driver
        self.search_textbox = "//input[@id='search_query_top']"
        self.submit_search_button = "//button[@name='submit_search']"
        self.item_xpath = "//div[@id='left_column']//li[4]//a[1]//img[1]"
        self.add_item = "//span[contains(text(),'Add to cart')]"
        self.check_out_xpath = "//span[contains(text(),'Proceed to checkout')]"


    def search_item(self,item):
        self.driver.find_element_by_xpath(self.search_textbox).send_keys(item)
        self.driver.find_element_by_xpath(self.submit_search_button).click()

    def choose_item(self):
        #self.driver.implicity_wait(5)
        self.driver.execute_script("window.scrollBy(0,500) ", "")
        self.driver.save_screenshot("C:/Users/Olga/PycharmProjects/SeleniumIntroduction/MCC/Screenshots/cart.png")
        self.driver.find_element_by_xpath(self.item_xpath).click()
        #self.driver.implicity_wait(5)

    def add_item_to_cart(self):
        self.driver.find_element_by_xpath(self.add_item).click()


    def check_out(self):
        self.driver.find_element_by_xpath(self.check_out_xpath).click()


























