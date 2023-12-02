import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


def pytest_addoption(parser):
    parser.addoption("--browser", "-B", action="store", default="chrome", choices=("chrome", "firefox"),
                     help="choose your browser")
    parser.addoption("--url", "-U", action="store", default="https://sbis.ru", help="enter url")



@pytest.fixture
def browser(request):
    """ Фикстура инициализации браузера """
    browser = request.config.getoption("--browser")
    path_to_this_dir = r"D:\Learning\My projects\autotesting\tests"
    if browser == "chrome":
        options = webdriver.ChromeOptions()
        prefs = {"download.default_directory": path_to_this_dir, "safebrowsing.enabled": "false"}
        options.add_experimental_option("prefs", prefs)
        options.add_argument("--start-maximized")
        driver = webdriver.Chrome(options=options)
    elif browser == "firefox":
        profile = Options()
        profile.set_preference("browser.download.folderList", 2)
        profile.set_preference("browser.download.manager.showWhenStarting", False)
        profile.set_preference("browser.download.dir", path_to_this_dir)
        profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream")
        driver = webdriver.Firefox(options=profile)
    else:
        raise Exception(f"{request.param} is not supported!")
    driver.implicitly_wait(10)
    request.addfinalizer(driver.quit)
    driver.get(request.config.getoption('--url'))
    return driver
