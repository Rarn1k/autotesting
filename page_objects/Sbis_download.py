import os
import time

from selenium.webdriver.support.wait import WebDriverWait

from locators.Locator import Locator
from page_objects.common.BasePage import BasePage


def download_wait():
    seconds = 0
    dl_wait = True
    this_path = './tests'
    while dl_wait and seconds < 30:
        time.sleep(1)
        dl_wait = False
        files = os.listdir(this_path)
        print(os.listdir(this_path))
        for fname in files:
            if fname.endswith('.crdownload') or fname.endswith('.part'):
                dl_wait = True
        seconds += 1
    return seconds


class SbisDownload(BasePage):

    def open_sbis_plagin(self):
        time.sleep(1)
        self._click(Locator.sbis_plagin)
        return self

    def download_web(self):
        self._wait_for_visible(Locator.link_download_web)
        self._click(Locator.link_download_web)
        download_wait()
        return self

    def get_plugin_size(self):
        self._get_element_text(Locator.link_download_web)
        return self
