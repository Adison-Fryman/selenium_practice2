# base class for all of our pages, need to pass it a driver
from locators import *
from element import BasePageElement


# for element on page i want to access and manipulate, define a class that names the element,set locator
# this will inherit from BasePageElement the ability to __get__ and __set__ aka waits
#SearchTextElement will let me find search box and send text to it.
class SearchTextElement(BasePageElement):
    locator = 'q'


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


# inside page file going to define a class for every webpage we are going to test.

class MainPage(BasePage):
    #this is a descriptor ....https://www.youtube.com/watch?v=mMbVs17Vmo4
    search_text_element = SearchTextElement()

    def is_title_matches(self):
        return "Python" in self.driver.title

    def click_go_button(self):
        element = self.driver.find_element(*MainPageLocators.Go_button)
        element.click()


class SearchResultPage(BasePage):

    def is_results_found(self):
        # what is page_source?
        return "no results found." not in self.driver.page_source
