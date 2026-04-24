from selenium.webdriver.common.by import By

class HomePage:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://demoblaze.com/index.html')

    def click_galaxy_s6(self):
        galaxy_s6 = self.browser.find_element(By.XPATH, '//a[text()="Samsung galaxy s6"]')
        galaxy_s6.click()

    def click_monitor(self):
        monitors_page = self.browser.find_element(By.CSS_SELECTOR, '''[onclick="byCat('monitor')"]''')
        monitors_page.click()

    def check_products_count(self, count_items: int):
        monitor_cards = self.browser.find_elements(By.CSS_SELECTOR, 'div .col-lg-4.col-md-6.mb-4')
        assert len(monitor_cards) == 2