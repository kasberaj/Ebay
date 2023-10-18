import time

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Search_Product_by_filter:
    Sort_by_Category_click = (By.XPATH, "//button[@id='gh-shop-a']")
    # Wait
    Cellphones_Accessories_click = (By.XPATH, "//a[normalize-space()='Cell phones & accessories']")
    # wait
    Cellphones_and_Smartphones = (By.XPATH, "//a[contains(text(),'Cell Phones & Smartphones')]")
    # Scroll upto
    All_Filters_Click = (By.XPATH, "//button[@aria-label='All Filters']")
    # Scroll upto condition
    Filter1_Condition_click = (By.XPATH, "//div[@id='c3-mainPanel-condition']")
    Filter1_New_Checkbox_Click = (By.ID, "c3-subPanel-LH_ItemCondition_New_cbx")
    Filter1_Used_Checkbox_Click = (By.ID, "c3-subPanel-LH_ItemCondition_Used_cbx")

    Filter2_Price_click = (By.XPATH, "//div[@id='c3-mainPanel-price']")
    Filter2_Price1_Enter = (By.XPATH, "//input[@aria-label='Minimum Value, US Dollar']")
    Filter2_Price2_Enter = "//input[@aria-label='Maximum Value, US Dollar']"

    Filter3_Item_Location_click = (By.XPATH, "//div[@id='c3-mainPanel-location']")
    Filter3_Location_Radio_click = (By.XPATH, "//input[@value='North America']")

    Apply_Button_Click = (By.XPATH, "//button[@aria-label='Apply']")

    Result_Status_Next_Page_Arrow = (By.XPATH, "//a[@aria-label='Go to next search page']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 5)

    def click_on_search_by_category(self):
        self.driver.find_element(*Search_Product_by_filter.Sort_by_Category_click).click()

    def click_on_cellphones_and_accessories(self):
        self.driver.find_element(*Search_Product_by_filter.Cellphones_Accessories_click).click()

    def click_on_cellphones_and_smartphones(self):
        self.wait.until(expected_conditions.visibility_of_element_located(self.Cellphones_and_Smartphones))
        self.driver.find_element(*Search_Product_by_filter.Cellphones_and_Smartphones).click()

    def scroll_to_all_filters(self):
        self.driver.execute_script("arguments[0].scrollIntoView();",
                                   self.driver.find_element(*Search_Product_by_filter.All_Filters_Click))

    def click_on_all_filters(self):
        self.wait.until(expected_conditions.visibility_of_element_located(self.All_Filters_Click))
        self.driver.find_element(*Search_Product_by_filter.All_Filters_Click).click()

    def scroll_upto_filter1_condition(self):
        self.driver.execute_script("arguments[0].scrollIntoView();",
                                   self.driver.find_element(*Search_Product_by_filter.Filter1_Condition_click))

    def click_on_filter1_condition(self):
        # self.wait.until(expected_conditions.visibility_of_element_located(self.Filter1_Condition_click))

        self.driver.find_element(*Search_Product_by_filter.Filter1_Condition_click).click()
        self.wait.until(expected_conditions.visibility_of_element_located(self.Filter1_New_Checkbox_Click))

        self.driver.find_element(*Search_Product_by_filter.Filter1_New_Checkbox_Click).click()
        self.driver.find_element(*Search_Product_by_filter.Filter1_Used_Checkbox_Click).click()

    def click_on_filter2_price(self):  # min_price, max_price)
        self.driver.find_element(*Search_Product_by_filter.Filter2_Price_click).click()
        time.sleep(5)
        # self.wait.until(expected_conditions.visibility_of_element_located(self.Filter2_Price1_Enter))

        # self.driver.find_element(*Search_Product_by_filter.Filter2_Price1_Enter).send_keys(min_price)
        # self.driver.find_element(*Search_Product_by_filter.Filter2_Price2_Enter).send_keys(max_price)

    def click_on_filter3_item_location(self):
        self.driver.find_element(*Search_Product_by_filter.Filter3_Item_Location_click).click()

        self.wait.until(expected_conditions.visibility_of_element_located(self.Filter3_Location_Radio_click))
        self.driver.find_element(*Search_Product_by_filter.Filter3_Location_Radio_click).click()

    def click_on_apply_button(self):
        self.driver.find_element(*Search_Product_by_filter.Apply_Button_Click).click()
        self.wait.until(expected_conditions.visibility_of_element_located(self.Result_Status_Next_Page_Arrow))

    def check_status(self):
        try:
            self.driver.find_element(*Search_Product_by_filter.Result_Status_Next_Page_Arrow)

            return 1
        except NoSuchElementException:
            return 0
