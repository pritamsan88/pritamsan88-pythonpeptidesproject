import pytest
from Utility.driver_setup import get_driver
from pages.searchpom import endtoendtesting
from pages.cartpage import cart


@pytest.fixture(scope="session")
def driver():
    driver = get_driver()
    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def endtoendtest(driver):
    return endtoendtesting(driver)


@pytest.fixture(scope="session")
def cartverify(driver):
    return cart(driver)


def test_Browseropen(endtoendtest):
    endtoendtest.open()


def test_gotopopulerproduct(endtoendtest):
    endtoendtest.gotopopularproducts()


def test_selectedpopulerproduct(endtoendtest):
    endtoendtest.selectedrandomproduct()


def test_anotherproductaddtocart(endtoendtest):
    endtoendtest.selectanotherproductaddtocart()


def test_carticonclick(cartverify):
    cartverify.clickcarticon()


def test_verifycartpage(cartverify):
    cartverify.verifycartpage()

def test_clickbuynow(cartverify):
    cartverify.clickbuynow()