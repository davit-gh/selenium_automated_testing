import unittest
from webdriver import Driver
from values import strings
from pageobjects.loginscreen import LoginScreen


class TestTechBuddyBookingPage(unittest.TestCase):

    def setUp(self):
        self.driver = Driver()
        self.driver.navigate(strings.base_url)

    def test_category_dropdown_booking_1a(self):
        loginscreen = LoginScreen(self.driver)
        bookingscreen = loginscreen.login_positive()
        bookingscreen.new_booking_button_click()
        bookingscreen.dropdown_is_displayed()
        bookingscreen.check_dropdown_options()

    def test_date_field_booking_1b(self):
        loginscreen = LoginScreen(self.driver)
        bookingscreen = loginscreen.login_positive()
        bookingscreen.new_booking_button_click()
        bookingscreen.date_field_is_displayed()
        bookingscreen.date_field_label_is_displayed()
        bookingscreen.date_popup_displayed_after_click()

    def test_textarea_field_booking_1c(self):
        loginscreen = LoginScreen(self.driver)
        bookingscreen = loginscreen.login_positive()
        bookingscreen.new_booking_button_click()
        bookingscreen.textarea_field_is_displayed()
        bookingscreen.textarea_label_is_displayed()

    def test_stored_address_checkbox_booking_1d(self):
        loginscreen = LoginScreen(self.driver)
        bookingscreen = loginscreen.login_positive()
        bookingscreen.new_booking_button_click()
        bookingscreen.stored_address_checkbox_label_is_displayed()
        bookingscreen.stored_address_checkbox_is_displayed()
        bookingscreen.stored_address_checkbox_is_checked_by_default()
        bookingscreen.stored_address_checkbox_click()
        bookingscreen.additional_address_input_field_is_displayed()
        bookingscreen.additional_zipcode_input_field_is_displayed()
        bookingscreen.additional_city_input_field_is_displayed()
        bookingscreen.additional_map_displayed()

    def test_price_boxes_booking_1e(self):
        loginscreen = LoginScreen(self.driver)
        bookingscreen = loginscreen.login_positive()
        bookingscreen.new_booking_button_click()
        bookingscreen.price_boxes_are_displayed()
        bookingscreen.click_first_price_box()
        bookingscreen.first_pricebox_becomes_active()
        bookingscreen.click_second_price_box()
        bookingscreen.second_pricebox_becomes_active()
        bookingscreen.click_terms_popup_link(bookingscreen.agreement2_link_locator)
        bookingscreen.terms_popup_is_opened(bookingscreen.terms2_dialog_locator)

    def test_reserve_button_booking_1f(self):
        loginscreen = LoginScreen(self.driver)
        bookingscreen = loginscreen.login_positive()
        bookingscreen.new_booking_button_click()
        bookingscreen.terms_checkbox_is_unchecked()
        bookingscreen.reserve_button_is_disabled()
        bookingscreen.click_terms_checkbox()
        bookingscreen.terms_checkbox_is_checked()
        bookingscreen.reserve_button_is_enabled()
        bookingscreen.click_terms_popup_link(bookingscreen.agreement1_link_locator)
        bookingscreen.terms_popup_is_opened(bookingscreen.terms1_dialog_locator)

    def tearDown(self):
        self.driver.instance.quit()


if __name__ == "__main__":
    unittest.main()