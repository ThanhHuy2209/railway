import allure
from pageObjects.GereralPage.GeneralPage import GeneralPage
from common.contants.contants import Contants
from testCases.TestBase import TestBase
from selenium.webdriver.remote.remote_connection import LOGGER


class TC03(TestBase):
    @allure.step("bookticket")
    def test_TC03(self):
        driver = self.driver
        generalPage = GeneralPage(driver)

        LOGGER.info("Step 1. Navigate to Railway Website")
        driver.get(Contants.RAILWAY_URL)

        LOGGER.info("Step 2. Go to BookticketPage")
        generalPage.gotoBookTicketPage()
