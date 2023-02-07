import constants
from lib.driver import get_driver
from lib.actions import Actions


class GetUrlTest:

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
        self.actions.take_screenshot("test.png")