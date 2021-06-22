from selenium.webdriver.common.by import By


class Login:
    def __init__(self, driver):
        self._driver = driver
        self._username = "//input[@id='username']"
        self._password = "//input[@id='password']"
        self._btn_Login = "//input[@value='login']"

    def enterAccount(self, username, password):
        self._driver.find_element(By.XPATH, self._username).send_keys(username)
        self._driver.find_element(By.XPATH, self._password).send_keys(password)

    def clickBtnLogin(self):
        self._driver.find_element(By.XPATH, self._btn_Login).click()
