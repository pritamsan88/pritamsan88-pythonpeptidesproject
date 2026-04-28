import time
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class checkoutsection:
    def __init__(self, driver: WebDriver):
        self.driver: WebDriver = driver
        self.loginbutton = (By.XPATH, "//a[text()='Log in']")
        self.loginemailaddress = (By.XPATH, "//input[@name='username']")
        self.loginpassword = (By.CSS_SELECTOR, "#password")
        self.login_button = (By.XPATH, "//button[@name='login']")

    def clickloginoncheckoutpage(self):
        wait = WebDriverWait(self.driver, 120)
        wait.until(EC.element_to_be_clickable(self.loginbutton)).click()
        time.sleep(3)
        wait.until(EC.presence_of_element_located(self.loginemailaddress)).send_keys("abhijit56@yopmail.com")
        wait.until(EC.presence_of_element_located(self.loginpassword)).send_keys("Sanyal88@")
        time.sleep(3)
        login_element = self.driver.find_element(*self.login_button)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", login_element)
        login_element.click()
        time.sleep(3)
