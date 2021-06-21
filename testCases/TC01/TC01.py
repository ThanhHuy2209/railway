import allure
from pageObjects.general.GeneralPage import GeneralPage
from common.contants.contants import Contants
from pageObjects.login.LoginPage import Login
from testCases.TestBase import TestBase


class TC01(TestBase):
    @allure.step("login")
    def TC01(self):
        driver = self.driver

        generalPage = GeneralPage(driver)

        print("Step 1. Navigate to Railway Website")
        driver.get(Contants.RAILWAY_URL)

        print("Step 2. Go to LoginPage")
        generalPage.gotoLoginPage()

        print("Step 3. Enter Account")
        Login.enterAccount(driver, Contants.USERNAME_RAILWAY, Contants.PASSWORD_RAILWAY)

        print("Step 4. Click to button")
        Login.clickBtnLogin(driver)
