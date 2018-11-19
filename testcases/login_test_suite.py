import unittest
from webdriver import Driver
from values import strings
from pageobjects.loginscreen import LoginScreen


class TestTechBuddyLogin(unittest.TestCase):

    def setUp(self):
        self.driver = Driver()
        self.driver.navigate(strings.base_url)

    def test_login_positive_login1a(self):
        login_screen = LoginScreen(self.driver)
        login_screen.page_title_equals_to("Boka en TechBuddy")
        login_screen.icon_is_displayed()
        login_screen.login_positive()

    def test_incorrect_mobile_number_alphabetical_login1b(self):
        login_screen = LoginScreen(self.driver)
        login_screen.mobile_number_field_is_displayed()
        login_screen.submit_button_is_displayed()
        login_screen.set_mobile_number(strings.incorrect_mobile_number_alphabetical)
        login_screen.click_submit()
        login_screen.error_inline_is_displayed()

    def test_incorrect_mobile_number_digits_login1c(self):
        login_screen = LoginScreen(self.driver)
        login_screen.mobile_number_field_is_displayed()
        login_screen.submit_button_is_displayed()
        login_screen.set_mobile_number(strings.incorrect_mobile_number_digits)
        login_screen.click_submit()
        login_screen.error_popup_is_displayed()

    def test_correct_mobile_number_incorrect_code_login1d(self):
        login_screen = LoginScreen(self.driver)
        login_screen.mobile_number_field_is_displayed()
        login_screen.submit_button_is_displayed()
        login_screen.set_mobile_number(strings.correct_mobile_number)
        login_screen.click_submit()
        label = login_screen.wait_until_element_label_is_displayed()
        login_screen.sms_code_field_is_displayed()
        login_screen.submit_button_is_displayed()
        login_screen.set_sms_code(strings.incorrect_sms_code)
        login_screen.click_submit()
        login_screen.error_inline_is_displayed()

    def tearDown(self):
        self.driver.instance.quit()


if __name__ == "__main__":
    unittest.main()