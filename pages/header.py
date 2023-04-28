from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Header(Page):
    SEARCH_BTN = (By.XPATH, '//*[@id="shopify-section-header"]/sticky-header/header/search-modal/details/summary/span')
    SEARCH_FIELD = (By.CSS_SELECTOR, '#Search-In-Modal')
    SPF_RESULT = (By.XPATH, '//span[@class="predictive-search__item-heading h4"]')

    def click_search_button(self):
        self.click(*self.SEARCH_BTN)

    def input_search_text(self, text):
        self.input_text(text, *self.SEARCH_FIELD)

    def verify_spf_result(self):
        elem = self.find_elements(*self.SPF_RESULT)
        for i in elem:
            assert "SPF" in (i.text)











