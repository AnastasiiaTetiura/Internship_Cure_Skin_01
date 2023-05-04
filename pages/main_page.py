from support.logger import logger
from pages.base_page import Page


class MainPage(Page):

    def open_main(self):
        logger.info('Opening url https://shop.cureskin.com/...')
        self.open_url('https://shop.cureskin.com/')