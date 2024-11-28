import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("http://137.132.92.226:4001/")
    page.get_by_placeholder("Email address*").fill("zhongkai@nus.edu.sg")
    page.get_by_placeholder("Password*").fill("123")
    page.get_by_role("button", name="Login").click()

    # create empty patent

        # empty field
    page.locator("a").filter(has_text="Patents").click()
    page.get_by_role("button", name="Create").click()
    page.get_by_text("Create New Patent").click()
    page.get_by_role("button", name="Create").click()
    expect(page.get_by_text("Please complete all required")).to_be_visible()

        # fill in 
    page.get_by_placeholder("Enter a title for this").click()
    page.get_by_placeholder("Enter a title for this").fill("test")
    page.get_by_role("combobox").first.click()
    page.get_by_placeholder("Search", exact=True).click()
    page.get_by_placeholder("Search", exact=True).fill("systems and method")
    page.locator("span").filter(has_text="Systems and method").first.click()
    page.get_by_role("button", name="Create").click()
    expect(page.get_by_role("alert")).not_to_be_visible()

    # import Patent
    page.locator(".MuiBox-root > .MuiPaper-root > .MuiToolbar-root > a").click()
    page.locator("a").filter(has_text="Patents").click()
    page.get_by_role("button", name="Create").click()
    page.get_by_text("Import Existing Patent").click()
    page.get_by_text("Select an associated").click()
    page.get_by_placeholder("Search", exact=True).click()
    page.get_by_placeholder("Search", exact=True).fill("systems and method")
    page.locator("span").filter(has_text="Systems and method").first.click()
    page.get_by_placeholder("e.g., CNxxxxxxxxA;").click()
    page.get_by_placeholder("e.g., CNxxxxxxxxA;").fill("US11810080B2")
    page.get_by_text("World Intellectual Property").click()
    page.get_by_text("United States Patent").click()
    page.get_by_role("button", name="Import").click()

    # wait and expect
    expect(page.get_by_text("Status")).to_be_visible(timeout=15000)
