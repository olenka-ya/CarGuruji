from selenium import webdriver
from selenium.webdriver.support.ui import Select


class checkOutPage():

    def __init__(self, driver):
        self.driver = driver
        self.proceed_to_checkout_button = "//a[@class='button btn btn-default standard-checkout button-medium']//span[contains(text(),'Proceed to checkout')]"
        self.bill_firstname_xpath = "/html[1]/body[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[1]/form[1]/div[1]/input[1]"
        self.bill_lastname_xpath = "//input[@id='lastname']"
        self.bill_street_address = "//input[@id='address1']"
        self.bill_city = "//input[@id='city']"
        self.bill_state_drdw = "//select[@id='id_state']"
        self.bill_postcode = "//input[@id='postcode']"
        self.bill_phone = "//input[@id='phone']"
        self.save_button = "//span[contains(text(),'Save')]"
        self.continue_checkout = "//button[@name='processAddress']//span[contains(text(),'Proceed to checkout')]"
        self.ship_proceed_to_check_out = "//button[@name='processCarrier']//span[contains(text(),'Proceed to checkout')]"
        self.choose_payment_method = "//a[@class='bankwire']"
        self.confirm_xpath = "//span[contains(text(),'I confirm my order')]"

    def proceed_check_out(self):
       self.driver.find_element_by_xpath(self.proceed_to_checkout_button).click()

    def enter_firstname(self, firstname):
        self.driver.find_element_by_xpath(self.bill_firstname_xpath).clear()
        self.driver.find_element_by_xpath(self.bill_firstname_xpath).send_keys(firstname)
        #self.driver.implicity_wait(10)

    def enter_bill_lastname(self, lastname):
        self.driver.find_element_by_xpath(self.bill_lastname_xpath).clear()
        self.driver.find_element_by_xpath(self.bill_lastname_xpath).send_keys(lastname)
        #self.driver.implicity_wait(10)

    def enter_bill_street(self,street):
        self.driver.find_element_by_xpath(self.bill_street_address).send_keys(street)

    def enter_bill_city(self,city):
        self.driver.find_element_by_xpath(self.bill_city).send_keys(city)

    def select_bill_state(self,sta):
        value = self.driver.find_element_by_xpath("//select[@id='id_state']")
        drp = Select(value)
        drp.select_by_visible_text(sta)

    def enter_bill_postcode(self,postcode):
        self.driver.find_element_by_xpath(self.bill_postcode).send_keys(postcode)

    def select_bill_country(self,coun):
        value = self.driver.find_element_by_xpath("//select[@id='id_country']")
        drp = Select(value)
        drp.select_by_visible_text(coun)

    def enter_bill_phone(self, phone):
        self.driver.find_element_by_xpath(self.bill_phone).clear()
        self.driver.find_element_by_xpath(self.bill_phone).send_keys(phone)

    def save(self):
        self.driver.find_element_by_xpath(self.save_button).click()

    def cont_check_out(self):
        self.driver.find_element_by_xpath(self.continue_checkout).click()
        self.driver.find_element_by_xpath("//input[@id='cgv']").click()
        self.driver.find_element_by_xpath(self.ship_proceed_to_check_out).click()

    def choose_payment(self):
        self.driver.find_element_by_xpath(self.choose_payment_method).click()

    def confirm(self):
        self.driver.find_element_by_xpath(self.confirm_xpath).click()

