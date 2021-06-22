import allure
from pageObjects.GereralPage.GeneralPage import GeneralPage
from common.contants.contants import Contants
from pageObjects.login.LoginPage import Login
from testCases.TestBase import TestBase
from utilities.utils import Utils

class TC02(TestBase):
    @allure.step("login")
    def test_TC02(self):
        driver = self.driver

        generalPage = GeneralPage(driver)

        print("Step 1. Navigate to Railway Website")
        driver.get(Contants.RAILWAY_URL)
        Utils.reportImage(self, "1.Navigate to Ebay Website")

        print("Step 2. Go to LoginPage")
        generalPage.gotoLoginPage()
        Utils.reportImage(self, "Step 2. Go to LoginPage")

        print("Step 3. Enter Account error")
        login = Login(driver)
        login.enterAccount(Contants.USERNAME_RAILWAY, Contants.PASSWORD_RAILWAY)
        Utils.reportImage(self, "Step 3. Enter Account error")

        print("Step 4. Click to button")
        login.clickBtnLogin()
        Utils.reportImage(self, "Step 4. Click to button")