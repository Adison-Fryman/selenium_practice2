from selenium.webdriver.support.ui import WebDriverWait


# watch out of xpath conversions when setting up these functions

# techwithtim selenium unit test video #2 min 6
class BasePageElement(object):
    # this is a dunder method-data model
    def __set__(self, obj, value):
        driver = obj.driver
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element_by_name(self.locator))
        # im not sure why it is clearing and sending keys in the __set__
        driver.find_element_by_name(self.locator).clear()
        driver.find_element_by_name(self.locator).send_keys(value)

    # techwithtim selenium unit test video #2 min 8.12
    def __get__(self, obj, owner):
        driver = obj.driver
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element_by_name(self.locator))
        element = driver.find_element_by_name(self.locator)
        return element.get_attribute("value")
