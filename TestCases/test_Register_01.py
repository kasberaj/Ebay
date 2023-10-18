import time

import pytest

from PageObjects.RegisterPage import Register_Page

from utilities.logger import Log_Generator


class Test_Register_User:
    log = Log_Generator.log_gen()   # Imported Log_Generator class to generate logs

    # @pytest.skip    # Using decorators to skip the test case
    def test_sign_in_001(self, setup):
        self.driver = setup  # Calling setup method from conftest file
        self.RP = Register_Page(self.driver)  # Created variable for accessing all methods from Register Page

        self.log.info("click on register")  # Writing logs
        self.RP.click_on_register()

        self.log.info("click on personal account")
        self.RP.click_on_personal_account_radio_button()

        self.log.info("enter first name")
        self.RP.enter_first_name('Raj')

        self.log.info("enter last name")
        self.RP.enter_last_name('Kasbe')

        self.log.info("enter email")
        self.RP.enter_email('Kasbe1@gmail.com')

        self.log.info("password")
        self.RP.enter_password('the@1997')

        self.RP.click_on_register_button()
        time.sleep(3)

        if self.RP.check_register_status() == True:
            self.log.info("Take screenshot after successful registration")
            self.driver.save_screenshot(
                "C:\\Users\\Raj\\PycharmProjects\\Cermati\\SceenShots\\test_sign_in_001_pass.png")
            print(" Successfully Registered")
            assert True
        else:
            self.driver.save_screenshot(
                "C:\\Users\\Raj\\PycharmProjects\\Cermati\\SceenShots\\test_sign_in_001_failed.png")
            assert False
