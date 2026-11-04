from playwright.sync_api import Page, expect


def test_login_page_title(page: Page):
    page.goto("https://www.saucedemo.com")
    expect(page).to_have_title("Swag Labs")


def test_successful_login(page: Page):
    page.goto("https://www.saucedemo.com")
    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("secret_sauce")
    page.locator("#login-button").click()
    expect(page.locator('[data-test="title"]')).to_have_text("Products")


def test_login_with_invalid_password(page: Page):
    page.goto("https://www.saucedemo.com")
    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("wrong_pass123")
    page.locator("#login-button").click()
    expect(page.locator('[data-test="error"]')).to_have_text("Epic sadface: Username and password do not match any user in this service")


def test_login_with_empty_username(page: Page):
    page.goto("https://www.saucedemo.com")
    page.locator("#password").fill("secret_sauce")
    page.locator("#login-button").click()
    expect(page.locator('[data-test="error"]')).to_have_text("Epic sadface: Username is required")


def test_login_with_empty_password(page: Page):
    page.goto("https://www.saucedemo.com")
    page.locator("#user-name").fill("standard_user")
    page.locator("#login-button").click()
    expect(page.locator('[data-test="error"]')).to_have_text("Epic sadface: Password is required")


def test_login_with_locked_out_user(page: Page):
    page.goto("https://www.saucedemo.com")
    page.locator("#user-name").fill("locked_out_user")
    page.locator("#password").fill("secret_sauce")
    page.locator("#login-button").click()
    expect(page.locator('[data-test="error"]')).to_have_text("Epic sadface: Sorry, this user has been locked out.")