from pages.base_page import BasePage
from components.components import WebElements


class Demoqa(BasePage):

    def __init__(self, driver):
        self.base_url = "https://demoqa.com/"
        super().__init__(driver, self.base_url)
        self.text = WebElements(driver, '#app > footer > span')
        self.cd = WebElements(driver, '#app > div > div > div.home-body > div > div:nth-child(1)')
        self.text_between = WebElements(driver, 'div.col-12.mt-4.col-md-6')