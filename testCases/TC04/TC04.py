import allure
from pageObjects.GereralPage.GeneralPage import GeneralPage
from common.contants.contants import Contants
from testCases.TestBase import TestBase
from pageObjects.RegisterPage.RegisterPage import RegisterPage


class TC04(TestBase):
    @allure.step("bookticket")
    def test_TC04(self):
        driver = self.driver
        generalPage = GeneralPage(driver)

        print("Step 1. Navigate to Railway Website")
        driver.get(Contants.RAILWAY_URL)

        print("Step 2. Go to BookticketPage")
        generalPage.gotoRegisterPage()

        print("Step 3. Enter valid information into all fields except Confirm Password is not same with password")
        registerPage = RegisterPage(driver)
        registerPage.enterAccount(Contants.USERNAME_RAILWAY, Contants.PASSWORD_RAILWAY, Contants.CONFIRM_PASSWORD, Contants.PID)

        print("Step 4. Click to button Register")
        registerPage.clickBtnLogin()

        print("VP. Message There're errors in the form. Please correct the error and try again.")
        self.assertTrue(registerPage.is_Message_Error_Display(), "Message error is not display.")
