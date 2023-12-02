import time

from locators.Locator import Locator
from page_objects.Sbis_download import SbisDownload
from page_objects.common.BasePage import BasePage


class Sbis(BasePage):

    def open_contacts(self):
        self._click(Locator.contacts)
        return self

    def open_page(self):
        return Sbis(self.driver)

    def download_sbis(self):
        self._scroll_to_element(Locator.download_sbis)
        self._wait_for_visible(Locator.download_sbis)
        self._click_in_block(Locator.download_sbis)
        return SbisDownload(self.driver)
