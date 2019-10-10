import unittest
from selenium import webdriver
import time
import HtmlTestRunner
from selenium import webdriver
from MCC.Pages.Logout.Logout import LogoutPage
from MCC.Pages.Addtocart.Addtocart import addtocartPage
from MCC.Pages.Login.Login import LoginPage
from MCC.Pages.Checkout.Checkout import checkOutPage


class MCCTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:/Users/Olga/PycharmProjects/SeleniumIntroduction/MCC/Driver/chromedriver.exe")
        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()

    def test2(self):
        driver = self.driver
        driver.get("http://carguruji.com/shop/login?back=my-account#account-creation")

        login = LoginPage(driver)
        login.SignIn("bella@gmail.com", "Bell123")

        driver.save_screenshot("C:/Users/Olga/PycharmProjects/SeleniumIntroduction/MCC/Screenshots/login.png")

    def test3(self):
        driver = self.driver
        driver.get("http://carguruji.com/shop/my-account")

        add = addtocartPage(driver)
        add.search_item("dress")
        add.choose_item()
        add.add_item_to_cart()
        add.check_out()

        driver.save_screenshot("C:/Users/Olga/PycharmProjects/SeleniumIntroduction/MCC/Screenshots/cart.png")


    def test4(self):
        driver = self.driver
        driver.get("http://carguruji.com/shop/address?back=order.php%3Fstep%3D1")

        checkout = checkOutPage(driver)
        checkout.enter_firstname("Bella")
        checkout.enter_bill_lastname("Wong")
        checkout.enter_bill_street("22 Victoria Ave")

        checkout.enter_bill_city("Montgomery")
        checkout.select_bill_state("Alabama")
        checkout.enter_bill_postcode("36043")
        checkout.select_bill_country("United States")
        checkout.enter_bill_phone("6471112233")

        checkout.save()
        checkout.cont_check_out()
        checkout.choose_payment()
        checkout.confirm()

        driver.save_screenshot("C:/Users/Olga/PycharmProjects/SeleniumIntroduction/MCC/Screenshots/conf.png")


    def test5(self):
        driver = self.driver
        logout = LogoutPage(driver)
        logout.SignOut()

        driver.save_screenshot("C:/Users/Olga/PycharmProjects/SeleniumIntroduction/MCC/Screenshots/logout.png")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()

