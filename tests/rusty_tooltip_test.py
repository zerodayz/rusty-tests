from lib.driver import get_driver
from lib.actions import Actions
from selenium.webdriver.common.by import By


class RustyTooltipTest:
    def __init__(self, driver, url, test_name):
        self.driver = None
        self.driver_name = driver
        self.actions = None
        self.url = url
        self.test_name = test_name

    def setup_test(self):
        print("Running setup_test...")
        self.driver = get_driver(self.driver_name, False)
        self.actions = Actions(self.driver)
        self.actions.create_test_dir(self.test_name)

    def teardown_test(self):
        print("Running teardown_test...")
        self.driver.quit()

    def run_test(self):
        print("Running run_test...")
        self.actions.go(self.url)
        self.actions.login("demo", "demo")
        tooltip = (By.ID, "posts")
        tooltiptext = (By.CLASS_NAME, "tooltiptext")
        self.actions.hover(tooltip)
        # blog = (By.ID, "blog")
        self.actions.highlight(tooltiptext)
        self.actions.take_screenshot("tooltip.png")
        self.teardown_test()

