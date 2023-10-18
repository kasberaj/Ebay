from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Search_By_Product_Name:
    SearchBox_Enter = (By.XPATH, "//input[@id='gh-ac']")
    Sort_by_Category_click = (By.XPATH, "//button[@id='gh-shop-a']")
    Computers_Tablet_Click = (By.XPATH, "//a[normalize-space()='Computers & tablets']")
    Status_Check_Macbook = (By.XPATH, "//div[normalize-space()='MacBooks']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 5)  # For using Explicit wait

    def enter_product_name(self, product):
        self.driver.find_element(*Search_By_Product_Name.SearchBox_Enter).send_keys(product)

    def click_on_search_by_category(self):
        self.wait.until(expected_conditions.visibility_of_element_located(self.Sort_by_Category_click))
        self.driver.find_element(*Search_By_Product_Name.Sort_by_Category_click).click()

    def click_on_computers_and_tablets(self):
        self.wait.until(expected_conditions.visibility_of_element_located(self.Computers_Tablet_Click))
        self.driver.find_element(*Search_By_Product_Name.Computers_Tablet_Click).click()

    def check_search_status(self):
        try:
            self.wait.until(expected_conditions.visibility_of_element_located(self.Status_Check_Macbook))
            self.driver.find_element(*Search_By_Product_Name.Status_Check_Macbook)
            return True

        except NoSuchElementException:
            print('Element not found')
            return False
