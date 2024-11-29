import re
from playwright.sync_api import Page, expect


def test_sucess_login(page: Page) -> None:
    page.goto("http://137.132.92.226:4001/login")
    page.get_by_placeholder("Email address*").fill("ip8value_test@ip8value.com")
    page.get_by_placeholder("Password*").fill("123")
    page.get_by_role("button", name="Login").click()

    # expect there is no alert and contains the text "Inventions"
    expect(page.get_by_role("alert")).not_to_be_visible()
    expect(page.locator("a").filter(has_text=re.compile("Inventions"))).to_have_count(1)


def test_fail(page: Page) -> None:

    # wrong password
    page.goto("http://137.132.92.226:4001/login")
    page.get_by_placeholder("Email address*").fill("ip8value_test@ip8value.com")
    page.get_by_placeholder("Password*").fill("12")
    page.get_by_role("button", name="Login").click()

    alert = page.get_by_role("alert")
    expect(alert).to_be_visible()
    expect(alert).to_have_text("The password you entered is incorrect.")

    # wrong email
    page.get_by_placeholder("Email address*").fill("ip8value_test@ip8value.co")
    page.get_by_placeholder("Password*").fill("123")
    page.get_by_role("button", name="Login").click()

    alert = page.get_by_role("alert")
    expect(alert).to_be_visible()
    expect(alert).to_have_text("Account not found. Please check your email address.")
