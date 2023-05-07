from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Header(Page):
    SEARCH_BTN = (By.CSS_SELECTOR, '#shopify-section-header > sticky-header > header > div > search-modal > details > summary > span > svg.icon.icon-search.modal__toggle-open')
    #(By.XPATH, '//*[@id="shopify-section-header"]/sticky-header/header/search-modal/details/summary/span')
    SEARCH_FIELD = (By.CSS_SELECTOR, '#Search-In-Modal')
    SPF_RESULT = (By.XPATH, '//span[@class="predictive-search__item-heading h4"]')

    def click_search_button(self):
        self.wait_for_element_appear(*self.SEARCH_BTN)
        self.click(*self.SEARCH_BTN)
        #search_btn = self.find_element(*self.SEARCH_BTN)
        #search_btn.click()

    def input_search_text(self, text):
        self.wait_for_element_appear(*self.SEARCH_FIELD)
        self.input_text(text, *self.SEARCH_FIELD)

    def verify_spf_result(self):
        elem = self.find_elements(*self.SPF_RESULT)
        for i in elem:
            assert "SPF" in (i.text)












