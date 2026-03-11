import time

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class cart:
    def __init__(self, driver: WebDriver):
        self.driver: WebDriver = driver
        self.headercaerticon = (By.CSS_SELECTOR, "#cart_toggle>img")

    def clickcarticon(self):
        wait = WebDriverWait(self.driver, 60)
        wait.until(EC.element_to_be_clickable(self.headercaerticon)).click()
        time.sleep(5)

    def verifycartpage(self):
        listofelements = self.driver.find_elements(By.CSS_SELECTOR, "div.cart_sidepanel_cnct_dtl > h2 > a")
        for element in listofelements:
            text = element.text.strip()
            self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", element)
            print("Added product in the cart is :-  ", text)

