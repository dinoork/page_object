from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
            "Basket items are presented, but should not be"
            
    def should_be_text_about_empty_basket(self):
        empty_basket_text = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_TEXT).text
        assert empty_basket_text == "Your basket is empty. Continue shopping", \
            "Text about empty basket is not presented, but should be"