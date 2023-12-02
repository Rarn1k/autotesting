import time

from selenium.webdriver.support.wait import WebDriverWait

from locators.Locator import Locator
from page_objects.common.BasePage import BasePage
from selenium.webdriver.support import expected_conditions as EC


class Tenzor(BasePage):

    def find_block_content(self):
        return self._element(Locator.block_content_tenzor)

    def find_power_in_people(self):
        return self._get_element_text(Locator.power_in_people)

    def open_more(self):
        time.sleep(1)  # For Firefox
        self._scroll_to_element(Locator.more)
        self._wait_for_visible(Locator.more)
        time.sleep(1)  # For Firefox
        self._click_in_block(Locator.more)
        return self
