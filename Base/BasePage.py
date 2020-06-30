from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.keys import Keys
class BasePage:

    def __init__(self):
        self.driver = None


    def smart_wait(self,locator = None, wait_seconds=10,  locator_type = None):
        """Performs an explicit wait for a particular element"""
        try:
            loc = locator
            if locator_type == 'button':
                WebDriverWait(self.driver, wait_seconds).until(EC.element_to_be_clickable((By.XPATH, loc)))
            else:
                WebDriverWait(self.driver, wait_seconds).until(EC.presence_of_element_located((By.XPATH,loc)))
        except Exception as e:
            print(e + 'Exception')
            return False
        return True

    def click_element(self,locator):
        "Click the button supplied"
        result_flag = False
        try:
            self.smart_wait(self.driver, locator, locator_type='button')
            self.get_element(self.driver,locator).click()
            result_flag = True
            #time.sleep(wait_time)
        except Exception as e:

            print('Exception when clicking link with path: %s' % locator)
        return result_flag


    def get_element(self, locator,type=None):
        """Return the DOM element of the path or 'None' if the element is not found """
        self.smart_wait(locator)
        dom_element = None
        try:
            dom_element = self.driver.find_element(By.XPATH, locator)
        except Exception as e:
            print(str(e) + 'debug')
            print("Error" % (locator))
        return dom_element


    def get_elements(self,locator):
        self.smart_wait(locator)
        dom_elements = None
        try:
            dom_element = self.driver.find_elements(By.XPATH, locator)
        except Exception as e:
            print(str(e) + 'debug')
            print("Error" % (locator))
        return dom_elements
    def get_text(self, locator):
        "Return the text for a given path or the 'None' object if the element is not found"
        text = ''
        try:
            text = self.get_element(locator).text
        except Exception as e:
            print(e)
            return None
        else:
            return text
    def set_text(self, locator, value, clear_flag=True):
        "Set the value of the text field"
        text_field = None
        try:
            text_field = self.get_element(locator)
            if text_field is not None and clear_flag is True:
                try:
                    text_field.clear()
                except Exception as e:
                    print(str(e))
        except Exception as e:
            print("Check your locator-'%s,%s' in the conf/locators.conf file" % (locator[0], locator[1]))
        result_flag = False
        if text_field is not None:
            try:
                text_field.send_keys(value)
                result_flag = True
            except Exception as e:
                print('Could not write to text field: %s' % locator)
        return result_flag

    def scroll(self,locator,locx,locy):

        # self.driver.swipe() #we can do swipe by giving the cordinate value
        action=TouchAction(self.driver)
        # action.move_to()
        webelement=self.get_element(locator=locator)
        try:
            action.press(webelement).perform()
            action.move_to(x=locx, y=locy).perform()
        except Exception as e:
            print(e)
    def key_press_from_keyboard(self,locator):
        action = TouchAction(self.driver)
        webelement = self.get_element(locator=locator)
        try:
            self.set_text(locator=webelement,value=self.driver.sendkeys(Keys.RETURN))
        except Exception as e:
            print(e)
