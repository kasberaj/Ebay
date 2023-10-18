from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


# Created class For registration
class Register_Page:
    # Created variables for each object on register page
    Register_Click = (By.XPATH, "/html[1]/body[1]/header[1]/div[1]/ul[1]/li[1]/span[1]/span[1]/a[1]")
    Personal_Account_RadioButton_Click = (By.XPATH, "//input[@id='personalaccount-radio']")
    First_Name_Enter = (By.ID, "firstname")
    Last_Name_Enter = (By.ID, "lastname")
    Email_Enter = (By.ID, "Email")
    Password_Enter = (By.ID, "password")
    Register_Button_Click = (By.XPATH, "//button[@id='EMAIL_REG_FORM_SUBMIT']")
    Register_Status = (By.XPATH, "// button[ @ id = 'gh-ug']")

    # Created constructor to call driver
    def __init__(self, driver):
        self.driver = driver
        # Created variable to implement explicit wait
        self.wait = WebDriverWait(self.driver, 5)

    # Created unique method for each action performed on register page

    def click_on_register(self):
        self.wait.until(expected_conditions.visibility_of_element_located(self.Register_Click))
        # Here browser will wait until it won't find the element (max wait time is 5 sec)
        self.driver.find_element(*Register_Page.Register_Click).click()

    def click_on_personal_account_radio_button(self):
        self.driver.find_element(*Register_Page.Personal_Account_RadioButton_Click).click()

    def enter_first_name(self, f_name):  # Gave an argument for accepting first name from user
        self.driver.find_element(*Register_Page.First_Name_Enter).send_keys(f_name)

    def enter_last_name(self, l_name):  # Gave an argument for accepting first name from user
        self.driver.find_element(*Register_Page.Last_Name_Enter).send_keys(l_name)

    def enter_email(self, email):  # Gave an argument for accepting first name from user
        self.driver.find_element(*Register_Page.Email_Enter).send_keys(email)

    def enter_password(self, passwd):
        self.driver.find_element(*Register_Page.Password_Enter).send_keys(passwd)

    def click_on_register_button(self, ):  # Gave an argument for accepting first name from user
        self.driver.find_element(*Register_Page.Register_Button_Click).click()

    def check_register_status(self):
        try:
            self.wait.until(expected_conditions.visibility_of_element_located(self.Register_Status))
            self.driver.find_element(*Register_Page.Register_Status)

            return True
        except NoSuchElementException:

            return False
