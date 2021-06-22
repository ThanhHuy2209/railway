from selenium import webdriver
import allure
import unittest


@allure.severity(allure.severity_level.NORMAL)
class TestBase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="F:\Selenium_python\chromedriver.exe")
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        print("\nTest Completed...")


if __name__ == "__main__":
    print("hi hi hi ")
    unittest.main()
