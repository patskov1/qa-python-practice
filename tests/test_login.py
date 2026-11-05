from playwright.sync_api import Page, expect
from pages.login_page import LoginPage


def test_successful_login(page: Page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")
    expect(page.locator('[data-test="title"]')).to_have_text("Products")


def test_login_with_invalid_password(page: Page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("standard_user", "wrong_pass123")
    expect(login_page.error_message).to_have_text("Epic sadface: Username and password do not match any user in this service")