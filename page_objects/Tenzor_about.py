from locators.Locator import Locator
from page_objects.common.BasePage import BasePage


class TenzorAbout(BasePage):

    def find_working(self):
        return self._element(Locator.working)

    def get_images(self):
        self._wait_for_visible(Locator.images)
        return self._element(Locator.images, many=True)
