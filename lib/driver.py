from selenium.webdriver import Chrome, Firefox, Safari

import constants


def get_driver(driver, headless):
    if driver == "chrome":
        # at the moment only supports mac
        if constants.PLATFORM == "Darwin":
            if constants.PROCESSOR == "arm":
                driver_path = constants.DRIVER_DIR + "/mac/arm/chromedriver"
                return Chrome(driver_path)
            else:
                driver_path = constants.DRIVER_DIR + "/mac/intel/chromedriver"
                return Chrome(driver_path)
        return Chrome()
    elif driver == "firefox":
        if constants.PLATFORM == "Darwin":
            if constants.PROCESSOR == "arm":
                driver_path = constants.DRIVER_DIR + "/mac/arm/geckodriver"
                return Firefox(driver_path)
            else:
                driver_path = constants.DRIVER_DIR + "/mac/intel/geckodriver"
                return Firefox(driver_path)
    elif driver == "safari":
        return Safari()
    else:
        raise Exception("Invalid driver")

