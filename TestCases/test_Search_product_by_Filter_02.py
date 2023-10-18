import time

from PageObjects.Access_Product_By_Filter import Search_Product_by_filter


class Test_Search_By_Filter:

    def test_search_by_filter_001(self, setup):
        self.driver = setup
        self.SF = Search_Product_by_filter(self.driver)

        self.driver.implicitly_wait(50)

        self.SF.click_on_search_by_category()

        self.SF.click_on_cellphones_and_accessories()

        self.SF.click_on_cellphones_and_smartphones()

        self.SF.scroll_to_all_filters()

        self.SF.click_on_all_filters()
        # time.sleep(2)
        self.SF.scroll_upto_filter1_condition()

        # self.SF.click_on_filter1_condition()
        # time.sleep(5)
        self.SF.click_on_filter2_price()  # 250, 400

        self.SF.click_on_filter3_item_location()

        self.SF.click_on_apply_button()

        if self.SF.check_status() == 1:
            self.driver.save_screenshot("C:\\Users\\Raj\\PycharmProjects\\Cermati\\SceenShots"
                                        "\\test_search_by_filter_001_passed.png")

            assert True
        else:
            self.driver.save_screenshot("C:\\Users\\Raj\\PycharmProjects\\Cermati\\SceenShots"
                                        "\\test_search_by_filter_001_passed.png")
            assert False
