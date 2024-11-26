from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    revenue = (By.XPATH, "//div[text()='Revenue Calculator']")

    # Web element for Revenue Calculator menu
    def revenueCalculator(self):
        return self.driver.find_element(*HomePage.revenue)
