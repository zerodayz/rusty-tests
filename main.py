import platform

from tests.rusty_tooltip_test import RustyTooltipTest


def main():
    rusty = RustyTooltipTest(driver="chrome",
                             url="http://127.0.0.1:8000/login",
                             test_name="rusty_tooltip_test")
    rusty.setup_test()
    rusty.run_test()
    rusty.teardown_test()


if __name__ == "__main__":
    main()
