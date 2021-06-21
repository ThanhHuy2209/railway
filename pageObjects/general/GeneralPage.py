from selenium.webdriver.common.by import By
class GeneralPage():
    def __init__(self, driver):
        self._driver = driver
        self._login_button = "//a[@href='/Account/Login.cshtml']"
        self._bookTicket_button = "//span[text()=\"Book ticket\"]"

    def gotoLoginPage(self):
        self._driver.find_element(By.XPATH, self._login_button).click()

    def gotoBookTicketPage(self):
        self._driver.find_element(By.XPATH, self._bookTicket_button).click()