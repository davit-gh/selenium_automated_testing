import unittest
from webdriver import Driver
from values import strings
from pageobjects.loginscreen import LoginScreen
from pageobjects.bookingscreen import BookingValidatioScreen

class TestTechBuddyBookingValidation(unittest.TestCase):

    def setUp(self):
        self.driver = Driver()
        self.driver.navigate(strings.base_url)

    def test_category_dropdown_validation_booking2a(self):
        loginscreen = LoginScreen(self.driver)
        bookingscreen = loginscreen.login_positive()
        bookingscreen.new_booking_button_click()
        bookingscreen.click_terms_checkbox()
        bookingscreen.click_reserve_button()
        validation = BookingValidatioScreen(self.driver)
        validation.validation_error_message_is_displayed(
            validation.dropdown_locator,
            validation.validation_error_dropdown_xpath
        )
        validation.select_dropdown_first_option()
        bookingscreen.click_reserve_button()
        validation.validation_error_message_is_not_displayed(
            validation.dropdown_locator,
            validation.validation_error_dropdown_xpath
        )

    def test_textarea_validation_booking2c(self):
        loginscreen = LoginScreen(self.driver)
        bookingscreen = loginscreen.login_positive()
        bookingscreen.new_booking_button_click()
        bookingscreen.click_terms_checkbox()
        bookingscreen.click_reserve_button()
        validation = BookingValidatioScreen(self.driver)
        validation.validation_error_message_is_displayed(
            validation.textarea_field_locator,
            validation.validation_error_textarea_xpath
        )
        validation.type_sample_text_in_textarea(
            bookingscreen.textarea_field_locator,
            strings.sample_text
        )
        bookingscreen.click_reserve_button()
        validation.validation_error_message_is_not_displayed(
            validation.textarea_field_locator,
            validation.validation_error_textarea_xpath
        )

    def test_priceboxes_validation_booking2e(self):
        loginscreen = LoginScreen(self.driver)
        bookingscreen = loginscreen.login_positive()
        bookingscreen.new_booking_button_click()
        bookingscreen.click_terms_checkbox()
        bookingscreen.click_reserve_button()
        validation = BookingValidatioScreen(self.driver)
        validation.validation_error_message_is_displayed(
            validation.textarea_field_locator,
            validation.validation_error_price_xpath
        )
        validation.click_first_price_box()
        bookingscreen.click_reserve_button()
        validation.validation_error_message_is_not_displayed(
            validation.textarea_field_locator,
            validation.validation_error_price_xpath
        )

    def test_all_elements_validation_booking2f(self):
        loginscreen = LoginScreen(self.driver)
        bookingscreen = loginscreen.login_positive()
        bookingscreen.new_booking_button_click()
        validation = BookingValidatioScreen(self.driver)
        validation.select_dropdown_first_option()
        validation.type_sample_text_in_textarea(
            bookingscreen.textarea_field_locator,
            strings.sample_text
        )
        validation.click_first_price_box()
        validation.click_terms_checkbox()
        validation.click_reserve_button()
        validation.thanks_page_is_displayed()

    def tearDown(self):
        self.driver.instance.quit()


if __name__ == "__main__":
    unittest.main()