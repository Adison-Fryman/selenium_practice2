from selenium import webdriver
# service is required with my browser version
from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# this holds the browser window open (options)
# options = Options()
# options.add_experimental_option("detach", True)
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# non-options driver
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# don't need this now
# driver.get("https://www.python.org")

import unittest
import page

url = "https://www.python.org"


# gives access to methods, run all tests

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        # put varibles in here
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        # options driver below if needed
        # self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        self.driver.get(url)

    def test_search_python(self):
        mainPage = page.MainPage()
        assert mainPage.is_title_matches()
        mainPage.search_text_element = "pycon"
        mainPage.click_go_button()
        search_result_page = page.SearchResultPage(self.driver)
        assert search_result_page.is_result_found()

    def test_example(self):
        # auto run when running unittest because starts with test
        assert True

    def test_example2(self):
        # auto run when running unittest because starts with test
        assert False

    def not_a_test(self):
        pass

    def tearDown(self):
        self.driver.close()


class Navigate():
    pass


if __name__ == "__main__":
    unittest.main()
