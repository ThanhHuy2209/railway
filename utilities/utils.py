import allure
from allure_commons.types import AttachmentType
from appium.webdriver.common.touch_action import TouchAction

class Utils():

    def __init__(self, driver):
        self._driver = driver

    @staticmethod
    def scrollToBottom(self):
        SCROLL_DUR_MS = 3000
        window_size = self._driver.get_window_size()
        self.scroll_y_top = window_size['height'] * 0.2
        self.scroll_y_bottom = window_size['height'] * 0.8
        self.scroll_x = window_size['width'] * 0.5

        for i in range(3):
            actions = TouchAction(self._driver)
            actions.long_press(None, self.scroll_x, self.scroll_y_bottom, SCROLL_DUR_MS)
            actions.move_to(None, self.scroll_x, self.scroll_y_top)
            actions.perform()

    @staticmethod
    def reportImage(self, message):
        try:
            allure.attach(self.driver.get_screenshot_as_png(), name=message, attachment_type=AttachmentType.PNG)
        except:
            print("Can not screenshot")

    @staticmethod
    def wait(self, time):
        self._driver.implicitly_wait(time)