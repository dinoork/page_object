from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage): 
    def add_to_cart(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        button.click()
    
    def check_added_book_name(self):
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
        added_book_name = self.browser.find_element(*ProductPageLocators.ADDED_BOOK_NAME).text
        assert book_name == added_book_name, f"Name of Book | Expected {book_name} is equal {added_book_name}"
    
    def check_added_cart_price(self):
        book_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text
        added_cart_price = self.browser.find_element(*ProductPageLocators.ADDED_CART_PRICE).text
        assert book_price == added_cart_price, f"Price of book | Expected {book_price} is equal {added_cart_price}"