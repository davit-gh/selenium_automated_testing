from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from values import strings
from .basescreen import BaseScreen


class BookingScreen(BaseScreen):

    booking_btn_locator = (By.CLASS_NAME, "custom-info-btn")
    dropdown_locator = (By.CLASS_NAME, "select-box")
    date_field_locator = (By.NAME, "when-day")
    date_field_Label_locator = (By.XPATH, "//label[@for='when-day']")
    textarea_field_locator = (By.CLASS_NAME, "el-textarea")
    textarea_label_locator = (By.XPATH, "//div[@class='el-textarea']/preceding-sibling::h3")
    sa_checkbox_label_locator = (By.XPATH, "//label[contains(@class,'is-checked')]/span[last()]")
    sa_checkbox_locator = (By.XPATH, "//label[contains(@class,'is-checked')]")
    address_field_locator = (By.ID, "street-name")
    zipcode_field_locator = (By.XPATH, "//h3[text()='Postnummer']/following-sibling::div/input")
    city_field_locator = (By.XPATH, "//h3[text()='Stad']/following-sibling::div/input")
    map_locator = (By.ID, "map")
    price_boxes_locator = (By.CLASS_NAME, "price-boxes-container")
    first_pricebox_locator = (By.XPATH, "//div[contains(@class, 'price-group-container')][1]")
    second_pricebox_locator = (By.XPATH, "//div[contains(@class, 'price-group-container')][2]")
    agreement1_link_locator = (By.XPATH, "//span[@class='el-checkbox__label']//a")
    terms1_dialog_locator = (By.XPATH, "//div[contains(@class, 'terms-dialog')][1]")
    agreement2_link_locator = (By.CLASS_NAME, "link-to-aggreement")
    terms2_dialog_locator = (By.XPATH, "//div[contains(@class, 'terms-dialog')][2]")
    terms_checkbox_locator = (By.XPATH, "//div[@class='term-container']/label")
    reserve_button_locator = (By.XPATH, "//div[contains(@class,'submit-row')]/button")

    def dropdown_is_displayed(self):
        dropdown = self.select_element(self.dropdown_locator)
        assert dropdown.is_displayed()

    def check_dropdown_options(self):
        expected_option_values = [
            "Datorer och surfplattor", "Tv/Media", "Telefoni",
            "Wifi och nätverk", "Smarta Hemmet"
        ]
        dropdown = self.select_element(self.dropdown_locator)
        for value in expected_option_values:
            xpath = "//div[contains(text(), '{}')]".format(value)
            option = dropdown.find_element_by_xpath(xpath)
            assert option.is_enabled()

    def new_booking_button_is_displayed(self):
        booking_btn = self.select_element(self.booking_btn_locator)
        assert booking_btn.is_displayed()

    def new_booking_button_click(self):
        booking_btn = self.select_element(self.booking_btn_locator)
        self.driver.instance.execute_script("arguments[0].click();", booking_btn)

    def date_field_is_displayed(self):
        date_field = self.select_element(self.date_field_locator)
        assert date_field.is_displayed()

    def date_field_label_is_displayed(self):
        date_label = self.select_element(self.date_field_Label_locator)
        assert date_label.is_displayed()

    def date_popup_displayed_after_click(self):
        date_field = self.select_element(self.date_field_locator)
        assert "active" not in date_field.get_attribute('class')
        date_field.click()
        assert "active" in date_field.get_attribute('class')

    def textarea_field_is_displayed(self):
        textarea_field = self.select_element(self.textarea_field_locator)
        assert textarea_field.is_displayed()

    def textarea_label_is_displayed(self):
        textarea_label = self.select_element(self.textarea_label_locator)
        assert textarea_label.is_displayed()

    def stored_address_checkbox_is_displayed(self):
        sa_checkbox = self.select_element(self.sa_checkbox_locator)
        assert sa_checkbox.is_displayed()

    def stored_address_checkbox_label_is_displayed(self):
        sa_checkbox_label = self.select_element(self.sa_checkbox_label_locator)
        assert sa_checkbox_label.is_displayed()

    def stored_address_checkbox_is_checked_by_default(self):
        sa_checkbox = self.select_element(self.sa_checkbox_locator)
        assert sa_checkbox.get_attribute('aria-checked') == 'true'

    def stored_address_checkbox_click(self):
        sa_checkbox = self.select_element(self.sa_checkbox_locator)
        self.driver.instance.execute_script("arguments[0].click();", sa_checkbox)

    def additional_address_input_field_is_displayed(self):
        address_field = self.select_element(self.address_field_locator)
        assert address_field.is_displayed()

    def additional_zipcode_input_field_is_displayed(self):
        zipcode_field = self.select_element(self.zipcode_field_locator)
        assert zipcode_field.is_displayed()

    def additional_city_input_field_is_displayed(self):
        city_field = self.select_element(self.city_field_locator)
        assert city_field.is_displayed()

    def additional_map_displayed(self):
        map = self.select_element(self.map_locator)
        assert map.is_displayed()

    def price_boxes_are_displayed(self):
        price_boxes = self.select_element(self.price_boxes_locator)
        assert price_boxes.is_displayed()

    def click_first_price_box(self):
        first_pricebox = self.select_element(self.first_pricebox_locator)
        first_pricebox.click()

    def click_second_price_box(self):
        second_pricebox = self.select_element(self.second_pricebox_locator)
        second_pricebox.click()

    def first_pricebox_becomes_active(self):
        first_pricebox = self.select_element(self.first_pricebox_locator)
        assert "price-group-container-active" in first_pricebox.get_attribute("class")

    def second_pricebox_becomes_active(self):
        second_pricebox = self.select_element(self.second_pricebox_locator)
        assert "price-group-container-active" in second_pricebox.get_attribute("class")

    def click_terms_popup_link(self, link_locator):
        agreement_link = self.select_element(link_locator)
        agreement_link.click()

    def terms_popup_is_opened(self, dialog_locator):
        terms_dialog = self.select_element(dialog_locator)
        assert terms_dialog.is_displayed()

    def terms_checkbox_is_unchecked(self):
        terms_checkbox = self.select_element(self.terms_checkbox_locator)
        assert "is-checked" not in terms_checkbox.get_attribute("class")

    def click_terms_checkbox(self):
        terms_checkbox = self.select_element(self.terms_checkbox_locator)
        terms_checkbox.click()

    def terms_checkbox_is_checked(self):
        terms_checkbox = self.wait_until_clickable(self.terms_checkbox_locator)
        assert "is-checked" in terms_checkbox.get_attribute("class")

    def reserve_button_is_disabled(self):
        reserve_button = self.select_element(self.reserve_button_locator)
        assert not reserve_button.is_enabled()

    def reserve_button_is_enabled(self):
        reserve_button = self.wait_until_clickable(self.reserve_button_locator)
        assert reserve_button.is_enabled()

    def click_reserve_button(self):
        reserve_button = self.wait_until_clickable(self.reserve_button_locator)
        reserve_button.click()


class BookingValidatioScreen(BookingScreen):

    validation_error_textarea_xpath = \
        validation_error_dropdown_xpath = "./following-sibling::p[contains(@class, 'error-block')]"
    validation_error_price_xpath = "//div[contains(@class, 'price-boxes-container')]//p"
    thanks_header_locator = (By.XPATH, "//div[contains(@class, 'thanks-header')]")

    def validation_error_message_is_displayed(self, element_locator, error_xpath):
        element = self.select_element(element_locator)
        try:
            self.driver.instance.implicitly_wait(3)
            element.find_element_by_xpath(error_xpath)
            is_displayed = True
        except NoSuchElementException:
            is_displayed = False
        assert is_displayed

    def validation_error_message_is_not_displayed(self, element_locator, error_xpath):
        element = self.select_element(element_locator)
        try:
            self.driver.instance.implicitly_wait(3)
            element.find_element_by_xpath(error_xpath)
            not_displayed = False
        except NoSuchElementException:
            not_displayed = True
        assert not_displayed

    def select_dropdown_first_option(self):
        option = self.driver.instance.find_element_by_xpath('//div[@class="option"]')
        self.driver.instance.execute_script("arguments[0].click();", option)

    def type_sample_text_in_textarea(self, locator, txt):
        textarea_div = self.select_element(locator)
        textarea_field = textarea_div.find_element_by_xpath('./textarea')
        textarea_field.send_keys(txt)

    def thanks_page_is_displayed(self):
        thanks_header = self.select_element(self.thanks_header_locator)
        thanks_header.is_displayed()