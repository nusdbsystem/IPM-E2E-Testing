import re
from playwright.sync_api import Page, expect


def test_sucess_change_password(page: Page) -> None:
    page.goto("http://137.132.92.226:4001/login")
    page.get_by_placeholder("Email address*").fill("ip8value_test@ip8value.com")
    page.get_by_placeholder("Password*").fill("123")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("button", name="Edit profile").click()
    page.get_by_text("Password", exact=True).click()

    page.get_by_placeholder("New Password*", exact=True).fill("123")
    page.get_by_placeholder("Confirm New Password*").fill("123")
    page.get_by_role("button", name="Save Password").click()

    alert = page.get_by_role("alert")
    expect(alert).to_be_visible()
    expect(alert).to_have_text("Your password has been changed")

    # wrong_confirm_password
    page.get_by_placeholder("New Password*", exact=True).fill("123")
    page.get_by_placeholder("Confirm New Password*").fill("12")
    page.get_by_role("button", name="Save Password").click()

    expect(page.get_by_role("alert")).not_to_be_visible()
    expect(page.get_by_text("Passwords does not match.")).to_be_visible()

    # empty_fields
    page.get_by_placeholder("New Password*", exact=True).fill("123")
    page.get_by_placeholder("Confirm New Password*").fill("")
    page.get_by_role("button", name="Save Password").click()

    expect(page.get_by_role("alert")).not_to_be_visible()
    expect(page.get_by_text("All fields are required.")).to_be_visible()

    # clear one field, fill the other
    page.get_by_placeholder("New Password*", exact=True).fill("")
    expect(page.get_by_text("All fields are required.")).not_to_be_visible()

    page.get_by_placeholder("Confirm New Password*").fill("123")
    page.get_by_role("button", name="Save Password").click()

    expect(page.get_by_role("alert")).not_to_be_visible()
    expect(page.get_by_text("All fields are required.")).to_be_visible()
