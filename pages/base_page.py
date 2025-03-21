class BasePage:
    def __init__(self, driver, base_url = 'https://demoqa.com/'):
        self.driver = driver
        self.base_url = base_url

    def visit(self):
        return self.driver.get(self.base_url)

    def get_url(self):
        return self.driver.current_url

    def equal_url(self):
        if self.get_url() == self.base_url:
            return True
        else:
            return False