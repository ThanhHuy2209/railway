import allure
from pageObjects.GereralPage.GeneralPage import GeneralPage
from common.contants.contants import Contants
from pageObjects.login.LoginPage import Login
from testCases.TestBase import TestBase
from utilities.utils import Utils

class TC01(TestBase):
    @allure.step("login")
    def test_TC01(self):
        driver = self.driver

        generalPage = GeneralPage(driver)

        print("Step 1. Navigate to Railway Website")
        driver.get(Contants.RAILWAY_URL)
        Utils.reportImage(self, "1.Navigate to Ebay Website")

        print("Step 2. Go to LoginPage")
        generalPage.gotoLoginPage()
        driver.save_screenshot(".\\Screenshots\\"+"test_step2.png")
        Utils.reportImage(self, "Step 2. Go to LoginPage")

        print("Step 3. Enter Account")
        login = Login(driver)
        login.enterAccount(Contants.USERNAME_RAILWAY, Contants.PASSWORD_RAILWAY)
        Utils.reportImage(self, "Step 3. Enter Account")

        print("Step 4. Click to button")
        login.clickBtnLogin()
        Utils.reportImage(self, "Step 4. Click to button")