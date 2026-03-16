import time

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class cart:
    def __init__(self, driver: WebDriver):
        self.driver: WebDriver = driver
        self.headercaerticon = (By.CSS_SELECTOR, "#cart_toggle>img")
        self.cartname = (By.XPATH, "//h3[text()='Cart']")
        self.totalprice=(By.CSS_SELECTOR,"#total_ammount > span > bdi")

    def clickcarticon(self):
        wait = WebDriverWait(self.driver, 60)
        wait.until(EC.element_to_be_clickable(self.headercaerticon)).click()
        time.sleep(5)
        expected = "Cart"
        actual = self.driver.find_element(*self.cartname).text.strip()
        assert expected == actual, f"Expected text '{expected}' does not match actual text '{actual}'"
        print("cart icon is click and cart page is open")

    def verifycartpage(self):
        total = 0

        listofelements = self.driver.find_elements(By.CSS_SELECTOR, "div.cart_sidepanel_cnct_dtl > h2 > a")
        listofprices = self.driver.find_elements(By.CSS_SELECTOR, "div.addcrt_wrap > h6 > span > bdi")
        listofquantity = self.driver.find_elements(By.CSS_SELECTOR, " div.addcrt_wrap > div > input")

        for i, element in enumerate(listofelements):
            text = element.text.strip()
            self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", element)
            # print("Added product in the cart is :-  ", text)
            time.sleep(1)
            itemprice = ""
            quantity = ""

            if i < len(listofprices):
                price_text = listofprices[i].text.strip().replace('\n', '')
                itemprice = price_text.replace('$', '').replace(',', '').split('.')[0]
                # print("Item price:", itemprice)
            if i < len(listofquantity):
                quantity = listofquantity[i].get_attribute("value")
            print(f"Added product in the cart is :- {text} | Price: {itemprice} | Quantity: {quantity}")

            if itemprice and quantity:
                total += int(itemprice) * int(quantity)

        print(f"Total price is {total}")
        expectedprice = self.driver.find_element(*self.totalprice).text.replace("$", "").replace(",", "").strip().split(".")[0]
        assert str(total) == expectedprice, f"Expected total price '{total}' does not match actual total price '{expectedprice}'"
