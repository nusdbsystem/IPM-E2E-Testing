import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("http://137.132.92.226:4001/")
    page.get_by_placeholder("Email address*").fill("zhongkai@nus.edu.sg")
    page.get_by_placeholder("Password*").fill("123")
    page.get_by_role("button", name="Login").click()

    # create empty ip
    page.locator("a").filter(has_text="Inventions").click()
    page.get_by_role("button", name="Create").click()
    page.get_by_placeholder("Enter a title for this").click()
    page.get_by_placeholder("Enter a title for this").fill("test")
    page.get_by_role("button", name="Create").click()

    # import IP from Patent ID
    page.get_by_role("banner").get_by_role("link").click()
    page.get_by_role("link", name="Inventions").click()
    page.get_by_role("button", name="Create").click()
    page.get_by_text("Import").click()
    page.get_by_text("Patent Number").click()
    page.get_by_placeholder("e.g., CNxxxxxxxxA;").click()
    page.get_by_placeholder("e.g., CNxxxxxxxxA;").fill("US11810080B2")
    page.locator("span").filter(has_text="World Intellectual Property").first.click()
    page.get_by_text("United States Patent").click()
    page.get_by_role("button", name="Import").click()

    # wait and expect alert "File imported!"
    alert = page.get_by_role("alert")
    # expect(alert).to_be_visible({ "timeout": 15000 })
    expect(alert).to_have_text("File imported!", timeout=15000)

    # generate tech offer
    page.locator("a").filter(has_text="Sections11").click()
    page.get_by_role("button", name="Generate Tech offer").click()
    page.get_by_placeholder("Select section titles").click()
    page.get_by_role("option", name="Abstract Word Count:").click()
    page.get_by_role("option", name="SUMMARY Word Count:").click()
    page.get_by_role("option", name="DETAILED DESCRIPTION Word Count:").click()
    page.get_by_label("Close").click()
    page.get_by_placeholder("Select template").click()
    page.get_by_text("Default tech offer [English").click()
    page.get_by_role("button", name="Confirm").click()
    expect(page.get_by_role("alert")).not_to_be_visible()
    # expect "Content Generating" to be visible
    expect(page.get_by_text("Content Generating")).to_be_visible()

    # transfer IP ownership
    page.get_by_text("Advanced").click()
    page.get_by_role("button", name="Transfer").click()
    page.locator("div").filter(has_text=re.compile(r"^Select a user$")).nth(1).click()
    page.get_by_text("IP8Value成果转化主管 (ip8value_test").click()
    page.get_by_role("button", name="Transfer").click()
    expect(alert).to_be_visible()
    expect(alert).to_have_text("IP ownership has been transferred.")