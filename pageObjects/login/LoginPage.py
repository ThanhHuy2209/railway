from selenium.webdriver.common.by import By


class Login:
    def __init__(self, driver):
        self._driver = driver
        self.username = "//input[@id='username']"
        self.password = "//input[@id='password']"
        self.btnLogin = "//input[@value='login']"

    def enterAccount(self, USERNAME_RAILWAY, PASSWORD_RAILWAY):
        self._driver.find_element(By.XPATH, self.username).send_keys(USERNAME_RAILWAY)
        self._driver.find_element(By.XPATH, self.password).send_keys(PASSWORD_RAILWAY)

    def clickBtnLogin(self):
        self._driver.find_element(By.XPATH, self.btnLogin).click()
