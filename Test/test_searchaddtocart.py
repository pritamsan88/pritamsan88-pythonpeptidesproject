import pytest
from Utility.driver_setup import get_driver
from pages.searchpom import endtoendtesting


@pytest.fixture(scope="session")
def driver():
    driver = get_driver()
    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def endtoendtest(driver):
    return endtoendtesting(driver)


def test_Browseropen(endtoendtest):
    endtoendtest.open()


def test_gotopopulerproduct(endtoendtest):
    endtoendtest.gotopopularproducts()


def test_selectedpopulerproduct(endtoendtest):
    endtoendtest.selectedrandomproduct()


def test_anotherproductaddtocart(endtoendtest):
    endtoendtest.selectanotherproductaddtocart()
