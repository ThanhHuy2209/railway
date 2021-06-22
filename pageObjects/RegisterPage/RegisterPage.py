from selenium.webdriver.common.by import By


class RegisterPage:
    def __init__(self, driver):
        self._driver = driver
        self._username = "//input[@id='email']"
        self._password = "//input[@id='password']"
        self._confirm_password = "//input[@id='confirmPassword']"
        self._PID = "//input[@id='pid']"
        self._register_button = "//input[@value='Register']"
        self._message_error = "//p[@class='message error']"

    def enterAccount(self, username, password, confirm, pid):
        self._driver.find_element(By.XPATH, self._username).send_keys(username)
        self._driver.find_element(By.XPATH, self._password).send_keys(password)
        self._driver.find_element(By.XPATH, self._confirm_password).send_keys(confirm)
        self._driver.find_element(By.XPATH, self._PID).send_keys(pid)

    def clickBtnLogin(self):
        self._driver.find_element(By.XPATH, self._register_button).click()

    def is_Message_Error_Display(self):
        return self._driver.find_element(By.XPATH, self._message_error).isDisplayed()
