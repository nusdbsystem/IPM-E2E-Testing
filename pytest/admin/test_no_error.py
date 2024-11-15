import re
from playwright.sync_api import Page, expect


def test_no_error(page: Page) -> None:
    page.goto("http://137.132.92.226:4001/login")
    page.get_by_placeholder("Email address*").fill("ip8value_test@ip8value.com")
    page.get_by_placeholder("Password*").fill("123")
    page.get_by_role("button", name="Login").click()

    expect(page.get_by_role("alert")).not_to_be_visible()
    
    page.locator("a").filter(has_text="Inventions").click()
    expect(page.get_by_role("alert")).not_to_be_visible()

    page.get_by_role("link", name="Managed Inventions").click()
    expect(page.get_by_role("alert")).not_to_be_visible()

    page.get_by_role("link", name="Created Inventions").click()
    expect(page.get_by_role("alert")).not_to_be_visible()


    page.locator("a").filter(has_text="Patents").click()
    expect(page.get_by_role("alert")).not_to_be_visible()

    page.get_by_role("link", name="Relevant Patents").click()
    expect(page.get_by_role("alert")).not_to_be_visible()

    page.get_by_role("link", name="Created Patents").click()
    expect(page.get_by_role("alert")).not_to_be_visible()


    page.locator("a").filter(has_text="Agreements").click()
    expect(page.get_by_role("alert")).not_to_be_visible()

    page.get_by_role("link", name="Relevant Agreements").click()
    expect(page.get_by_role("alert")).not_to_be_visible()

    page.get_by_role("link", name="Created Agreements").click()
    expect(page.get_by_role("alert")).not_to_be_visible()

    page.locator("a").filter(has_text="Events").click()
    expect(page.get_by_role("alert")).not_to_be_visible()

    page.locator("a").filter(has_text="Organizations").click()
    expect(page.get_by_role("alert")).not_to_be_visible()

    page.locator("a").filter(has_text="Fundings").click()
    expect(page.get_by_role("alert")).not_to_be_visible()

    page.locator("a").filter(has_text="Dashboard").click()
    expect(page.get_by_role("alert")).not_to_be_visible()

    page.locator("a").filter(has_text="Settings").click()
    expect(page.get_by_role("alert")).not_to_be_visible()

    page.locator("a").filter(has_text="Users").click()
    expect(page.get_by_role("alert")).not_to_be_visible()