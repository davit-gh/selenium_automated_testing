from pageobjects.bookingscreen import BookingScreen
from selenium.webdriver.common.by import By
from values import strings
from .basescreen import BaseScreen


class LoginScreen(BaseScreen):
    """Models login functionality as a Page Object"""

    icon = (By.CLASS_NAME, "techbuddy-logo")
    mobile_field = code_field = (By.CLASS_NAME, "el-input__inner")
    submit_btn = (By.CLASS_NAME, "submit-button")
    input_lbl = (By.XPATH, "//h3[text()='Kod']")
    error_div = (By.CLASS_NAME, "el-notification__content")
    error_inline = (By.XPATH, "//p[@class='error-block']")

    def icon_is_displayed(self):
        icon = self.select_element(self.icon)
        assert icon.is_displayed()

    def wait_until_element_label_is_displayed(self):
        """Used for waiting for the screen update after a click"""
        input_lbl = self.select_element(self.input_lbl)
        return  input_lbl

    def error_popup_is_displayed(self):
        error_popup = self.select_element(self.error_div)
        assert error_popup.is_displayed()

    def error_inline_is_displayed(self):
        error_inline = self.select_element(self.error_inline)
        assert error_inline.is_displayed()

    def mobile_number_field_is_displayed(self):
        mobile_field = self.select_element(self.mobile_field)
        assert mobile_field.is_displayed()

    def sms_code_field_is_displayed(self):
        code_field = self.select_element(self.code_field)
        assert code_field.is_displayed()

    def submit_button_is_displayed(self):
        submit_btn = self.select_element(self.submit_btn)
        assert submit_btn.is_displayed()

    def set_mobile_number(self, mobile_number):
        mobile = self.select_element(self.mobile_field)
        mobile.send_keys(mobile_number)

    def set_sms_code(self, code):
        code_field = self.select_element(self.code_field)
        code_field.send_keys(code)

    def click_submit(self):
        submit_btn = self.select_element(self.submit_btn)
        submit_btn.click()

    def login_positive(self):
        self.mobile_number_field_is_displayed()
        self.submit_button_is_displayed()
        self.set_mobile_number(strings.correct_mobile_number)
        self.click_submit()
        label = self.wait_until_element_label_is_displayed()
        self.sms_code_field_is_displayed()
        self.submit_button_is_displayed()
        self.set_sms_code(strings.correct_sms_code)
        self.click_submit()
        bs = BookingScreen(self.driver)
        bs.new_booking_button_is_displayed()
        return bs

