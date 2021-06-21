import allure
from pageObjects.general.GeneralPage import GeneralPage
from common.contants.contants import Contants
from testCases.TestBase import TestBase


class TC03(TestBase):
    @allure.step("login")
    def TC03(self):
        driver = self.driver
        generalPage = GeneralPage(driver)

        print("Step 1. Navigate to Railway Website")
        driver.get(Contants.RAILWAY_URL)

        print("Step 2. Go to BookticketPage")
        generalPage.gotoBookTicketPage()
