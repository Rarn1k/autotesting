import time

from selenium.webdriver.support.wait import WebDriverWait

from locators.Locator import Locator
from page_objects.Tenzor import Tenzor
from page_objects.common.BasePage import BasePage


class SbisContacts(BasePage):
    def open_tenzor(self):
        self._click(Locator.tenzor)
        return self

    def get_region(self):
        time.sleep(1)
        return self._element(Locator.region)

    def get_partners(self):
        return self._element(Locator.list_container, many=True)

    def open_region(self):
        self._click(Locator.region)
        return SbisContacts(self._element(Locator.region_panel))

    def open_kamchatka(self):
        self._click_in_block(Locator.kamchatka)
        return self
