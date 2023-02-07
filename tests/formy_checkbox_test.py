import constants
from lib.driver import get_driver
from lib.actions import Actions
from selenium.webdriver.common.by import By


class FormyCheckboxTest:
    def __init__(self, driver, url, test_name):
        self.driver = None
        self.driver_name = driver
        self.actions = None
        self.url = url
        self.test_name = test_name

    def setup_test(self):
        print("Running setup_test...")
        self.driver = get_driver(self.driver_name)
        self.actions = Actions(self.driver)
        self.actions.create_test_dir(self.test_name)

    def teardown_test(self):
        print("Running teardown_test...")
        self.driver.quit()

    def run_test(self):
        print("Running run_test...")
        self.actions.go(self.url)
        # find the checkbox by id, click it, highlight it, take a screenshot
        checkboxes = ["checkbox-1", "checkbox-2", "checkbox-3"]
        for checkbox in checkboxes:
            # find the checkbox by id
            el = (By.ID, checkbox)
            # click it
            # highlight it
            # take a screenshot
            self.actions.click(el)
            self.actions.highlight(el)
            self.actions.take_screenshot(f"{checkbox}.png")
            self.actions.click(el)
        self.teardown_test()

