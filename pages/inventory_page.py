from playwright.sync_api import Page


class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.title = page.locator('[data-test="title"]')
        self.cart_badge = page.locator('[data-test="shopping-cart-badge"]')

    def add_to_cart(self, product_id):
        self.page.locator(f"#add-to-cart-{product_id}").click()