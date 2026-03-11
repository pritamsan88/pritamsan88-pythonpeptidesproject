from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.action_chains import ActionChains
import random


class endtoendtesting:
    def __init__(self, driver: WebDriver):
        self.driver: WebDriver = driver
        self.url = "https://updates.futuristicbug.com/peptidesciences/peptidesciences_wordpress/"
        self.header_popularproduct_scroll = (By.XPATH, "//h2[text()='POPULAR PEPTIDES']")
        self.searchbar = (By.XPATH, "//input[@placeholder='Search products...']")
        self.addtocartbuttoninproductdetailspage = (By.XPATH, "//button[@type='submit']/span")
        self.successadded = (By.CSS_SELECTOR, "div.addingtocartTextwrppr > p")
        self.headercarticon = (By.CSS_SELECTOR, "#cart_toggle > img")
        # self.listofelements = self.driver.find_elements(By.CSS_SELECTOR, "div.prd_card_des > h3 > a")

    def open(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        time.sleep(2)
        print("project url is open")

    def gotopopularproducts(self):
        populerproduct = self.driver.find_element(*self.header_popularproduct_scroll)
        time.sleep(3)
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", populerproduct)
        print("Go to populer product")
        time.sleep(1)

    def selectedrandomproduct(self):

        time.sleep(2)
        wait = WebDriverWait(self.driver, 60)

        wait.until(
            EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, "div.prd_card_des > h3 > a")
            )
        )
        self.listofelements = self.driver.find_elements(
            By.CSS_SELECTOR, "div.prd_card_des > h3 > a"
        )
        if not self.listofelements:
            print("Products are not found")
            return

        action = ActionChains(self.driver)
        random_index = random.randrange(len(self.listofelements))
        print(f"Random index of selected product id {random_index}")

        if random_index == 4:
            arrow = self.driver.find_element(
                By.CSS_SELECTOR, "button.slick-next.slick-arrow")
            arrow.click()
            time.sleep(2)

            ele = self.listofelements[random_index]
            ele_text = ele.text.strip()
            print(f"🎯 Random Product Selected: {ele_text}")

            product_card = ele.find_element(
                By.XPATH, "./ancestor::div[contains(@class,'prd_card')]"
            )
            action.move_to_element(product_card).perform()

            add_to_cart = product_card.find_element(
                By.CSS_SELECTOR, "div.price_wrp button"
            )
            wait = WebDriverWait(self.driver, 60)
            wait.until(EC.element_to_be_clickable(add_to_cart))

            self.driver.execute_script(
                "arguments[0].scrollIntoView(true);", add_to_cart)
            time.sleep(1)
            self.driver.execute_script("arguments[0].click();", add_to_cart)
            print("✅ Product added to cart")
            time.sleep(3)

        else:
            time.sleep(2)

            ele = self.listofelements[random_index]
            ele_text = ele.text.strip()
            print(f"🎯 Random Product Selected: {ele_text}")

            product_card = ele.find_element(
                By.XPATH, "./ancestor::div[contains(@class,'prd_card')]"
            )
            action.move_to_element(product_card).perform()

            add_to_cart = product_card.find_element(
                By.CSS_SELECTOR, "div.price_wrp button"
            )
            wait = WebDriverWait(self.driver, 60)
            wait.until(EC.element_to_be_clickable(add_to_cart))

            self.driver.execute_script("arguments[0].scrollIntoView(true);", add_to_cart)
            time.sleep(1)
            self.driver.execute_script("arguments[0].click();", add_to_cart)

            print("✅ Product added to cart")
            time.sleep(3)

    def selectanotherproductaddtocart(self):
        wait = WebDriverWait(self.driver, 80)
        wait.until(EC.presence_of_element_located(self.searchbar))
        searchbarenter = self.driver.find_element(*self.searchbar)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", searchbarenter)
        searchbarenter.send_keys("10mg")
        time.sleep(3)

        autosuggestion_locator = (By.CSS_SELECTOR,
                                  "div.d-none.d-lg-block.saerch_wrp > div > ul > li")

        wait.until(EC.visibility_of_all_elements_located(autosuggestion_locator))

        listofautosuggestionresult = self.driver.find_elements(*autosuggestion_locator)

        time.sleep(2)

        if listofautosuggestionresult:
            randomproduct = random.choice(listofautosuggestionresult)
            print("Selected:", randomproduct.text)
            time.sleep(1)
            randomproduct.click()
            time.sleep(1)
            addtocart = self.driver.find_element(*self.addtocartbuttoninproductdetailspage)
            self.driver.execute_script("arguments[0].scrollIntoView(true);", addtocart)
            self.driver.execute_script("arguments[0].click();", addtocart)
            # addtocart.click()

            sucess = self.driver.find_element(*self.successadded)
            wait.until(EC.visibility_of(sucess))
            time.sleep(2)

            alert = sucess.text.strip()
            print(f"result :{alert}")
            expected = "Successfully added to cart!"
            assert alert == expected
            time.sleep(2)
            element = self.driver.find_element(*self.headercarticon)
            self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", element)
            wait.until(EC.visibility_of(element))
            time.sleep(1)
            count = self.driver.find_element(By.ID, "header-cart-count").text.strip()
            if int(count) > 1:
                print("Product added to the cart :-", count)
            else:
                print("Product not added to the cart :-", count)


