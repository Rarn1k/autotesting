from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def _element(self, selector: dict, many: bool = False):
        by = None
        if 'link_text' in selector.keys():
            by = By.LINK_TEXT
            selector = selector['link_text']
        elif 'css' in selector.keys():
            by = By.CSS_SELECTOR
            selector = selector['css']
        elif 'class_name' in selector.keys():
            by = By.CLASS_NAME
            selector = selector['class_name']
        elif 'tag' in selector.keys():
            by = By.TAG_NAME
            selector = selector['tag']
        return self.driver.find_element(by, selector) if not many else self.driver.find_elements(by, selector)

    def _click(self, selector):
        ActionChains(self.driver).move_to_element(self._element(selector)).click().perform()

    def _click_in_block(self, selector):
        self._element(selector).click()

    def _wait_for_visible(self, selector, wait=3):
        return WebDriverWait(self.driver, wait).until(EC.visibility_of(self._element(selector)))

    def _get_element_text(self, selector):
        return self._element(selector).text

    def _scroll_to_element(self, selector):
        try:
            self._element(selector).send_keys(Keys.DOWN)
        except Exception as e:
            pass
