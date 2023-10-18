from PageObjects.Search_By_Name_Page import Search_By_Product_Name
from utilities.logger import Log_Generator


class Test_Search_By_Name:
    log = Log_Generator.log_gen()

    def test_search_product_003(self, setup):
        self.driver = setup  # Calling Browser from Conftest setup method
        self.SN = Search_By_Product_Name(self.driver)  # Created variable to access the Class

        self.log.info('Enter the product name')
        self.SN.enter_product_name('Macbook')
        self.SN.click_on_search_by_category()
        self.SN.click_on_computers_and_tablets()

        if self.SN.check_search_status() == True:
            print('Project Found')
            assert True
        else:
            print('Project is not in the search result')
            assert False
