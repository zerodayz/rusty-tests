from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.action_chains import ActionChains

import constants
import os


class Actions:

    def __init__(self, driver):
        self.driver = driver
        self.test_dir = None
        self.screenshot_dir = constants.SCREENSHOTS_DIR

    def go(self, url):
        self.driver.get(url)
        # wait for the page to load
        try:
            WebDriverWait(self.driver, 60).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
        except Exception as e:
            print("Error: ", e)
            self.driver.quit()
            raise e

    def create_test_dir(self, test_name):
        # create a directory for the test
        self.test_dir = os.path.join(constants.SCREENSHOTS_DIR, test_name)
        # check if the directory exists and remove it if it does
        if os.path.exists(self.test_dir):
            # inform the directory exists, do you want to remove it y/n?
            remove = input("Directory exists, do you want to remove it? [y/n]: ")
            if remove == "y":
                try:
                    # remove all files inside directory
                    for file in os.listdir(self.test_dir):
                        os.remove(os.path.join(self.test_dir, file))
                    # remove the directory
                    os.rmdir(self.test_dir)
                except Exception as e:
                    print("Error: ", e)
                    self.driver.quit()
                    raise e
            else:
                print("Directory not removed, exiting")
                self.driver.quit()
                raise Exception("Test Directory exists")
        # create the directory
        try:
            os.mkdir(self.test_dir)
        except Exception as e:
            print("Error: ", e)
            self.driver.quit()
            raise e

    def take_screenshot(self, filename):
        # save the screenshot to the screenshot directory + test directory
        dest_dir = os.path.join(self.screenshot_dir, self.test_dir)
        self.driver.save_screenshot(os.path.join(dest_dir, filename))

    def type(self, element, text):
        try:
            WebDriverWait(self.driver, 60).until(EC.presence_of_element_located(element))
            self.driver.find_element(*element).send_keys(text)
        except Exception as e:
            print("Error: ", e)
            self.driver.quit()
            raise e

    def highlight(self, element):
        # draw the square around the element
        try:
            WebDriverWait(self.driver, 60).until(EC.presence_of_element_located(element))
            self.driver.execute_script("arguments[0].style.border='5px solid red'",
                                       self.driver.find_element(*element))
        except Exception as e:
            print("Error: ", e)
            self.driver.quit()
            raise e

    def click(self, element):
        try:
            WebDriverWait(self.driver, 60).until(EC.presence_of_element_located(element))
            self.driver.find_element(*element).click()
        except Exception as e:
            print("Error: ", e)
            self.driver.quit()
            raise e

    def hover(self, element):
        try:
            WebDriverWait(self.driver, 60).until(EC.presence_of_element_located(element))
            hover = ActionChains(self.driver).move_to_element(self.driver.find_element(*element))
            hover.perform()
        except Exception as e:
            print("Error: ", e)
            self.driver.quit()
            raise e

    def login(self, username, password):
        # find the username and password fields
        # type the username and password
        # click the login button
        username_field = (By.NAME, "username")
        password_field = (By.NAME, "password")
        login_button = (By.CSS_SELECTOR, "button[type='submit']")
        self.type(username_field, username)
        self.type(password_field, password)
        self.click(login_button)
        # wait for the page to load
        try:
            WebDriverWait(self.driver, 60).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
        except Exception as e:
            print("Error: ", e)
            self.driver.quit()
            raise e
