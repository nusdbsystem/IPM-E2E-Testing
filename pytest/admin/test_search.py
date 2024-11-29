import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("http://137.132.92.226:4001/")
    page.get_by_placeholder("Email address*").fill("ip8value_test@ip8value.com")
    page.get_by_placeholder("Password*").fill("123")
    page.get_by_role("button", name="Login").click()

    page.locator("a").filter(has_text="Inventions").click()
    page.get_by_placeholder("Search...").click()
    page.get_by_placeholder("Search...").fill("test")
    page.get_by_placeholder("Search...").press("Enter")
    expect(page.get_by_role("alert")).not_to_be_visible()

    page.get_by_text("Publish", exact=True).click()
    expect(page.get_by_role("alert")).not_to_be_visible()

    page.locator("p").filter(has_text="Draft").click()
    expect(page.get_by_role("alert")).not_to_be_visible()

    page.get_by_text("Archive", exact=True).click()
    expect(page.get_by_role("alert")).not_to_be_visible()
    
    page.get_by_role("link", name="Managed Inventions").click()
    page.get_by_placeholder("Search...").click()
    page.get_by_placeholder("Search...").fill("test")
    page.get_by_placeholder("Search...").press("Enter")
    expect(page.get_by_role("alert")).not_to_be_visible()
    
    page.get_by_text("Publish", exact=True).click()
    expect(page.get_by_role("alert")).not_to_be_visible()
    
    page.locator("p").filter(has_text="Draft").click()
    expect(page.get_by_role("alert")).not_to_be_visible()
    
    page.get_by_text("Archive", exact=True).click()
    expect(page.get_by_role("alert")).not_to_be_visible()
    
    page.get_by_role("link", name="Created Inventions").click()
    page.get_by_placeholder("Search...").click()
    page.get_by_placeholder("Search...").fill("test")
    page.get_by_placeholder("Search...").press("Enter")
    expect(page.get_by_role("alert")).not_to_be_visible()
    
    page.get_by_text("Publish", exact=True).click()
    expect(page.get_by_role("alert")).not_to_be_visible()
    
    page.locator("p").filter(has_text="Draft").click()
    expect(page.get_by_role("alert")).not_to_be_visible()
    
    page.get_by_text("Archive", exact=True).click()
    expect(page.get_by_role("alert")).not_to_be_visible()
    
    page.locator("a").filter(has_text="Patents").click()
    page.get_by_placeholder("Search...").click()
    page.get_by_placeholder("Search...").fill("test")
    page.get_by_placeholder("Search...").press("Enter")
    expect(page.get_by_role("alert")).not_to_be_visible()
    
    page.get_by_role("link", name="Relevant Patents").click()
    page.get_by_placeholder("Search...").click()
    page.get_by_placeholder("Search...").fill("test")
    page.get_by_placeholder("Search...").press("Enter")
    expect(page.get_by_role("alert")).not_to_be_visible()
    
    page.get_by_role("link", name="Created Patents").click()
    page.get_by_placeholder("Search...").click()
    page.get_by_placeholder("Search...").fill("test")
    page.get_by_placeholder("Search...").press("Enter")
    expect(page.get_by_role("alert")).not_to_be_visible()
    
    page.locator("a").filter(has_text="Agreements").click()
    page.get_by_placeholder("Search...").click()
    page.get_by_placeholder("Search...").fill("test")
    page.get_by_placeholder("Search...").press("Enter")
    expect(page.get_by_role("alert")).not_to_be_visible()
    
    page.get_by_role("link", name="Relevant Agreements").click()
    page.get_by_placeholder("Search...").click()
    page.get_by_placeholder("Search...").fill("test")
    page.get_by_placeholder("Search...").press("Enter")
    expect(page.get_by_role("alert")).not_to_be_visible()
    
    page.get_by_role("link", name="Created Agreements").click()
    page.get_by_placeholder("Search...").click()
    page.get_by_placeholder("Search...").fill("test")
    page.get_by_placeholder("Search...").press("Enter")
    expect(page.get_by_role("alert")).not_to_be_visible()
    
    page.locator("a").filter(has_text="Organizations").click()
    page.get_by_placeholder("Search...").click()
    page.get_by_placeholder("Search...").fill("test")
    page.get_by_placeholder("Search...").press("Enter")
    expect(page.get_by_role("alert")).not_to_be_visible()
    
    page.get_by_text("University").click()
    expect(page.get_by_role("alert")).not_to_be_visible()
    
    page.get_by_text("Department").click()
    expect(page.get_by_role("alert")).not_to_be_visible()
    
    page.get_by_text("Faculty").click()
    expect(page.get_by_role("alert")).not_to_be_visible()
    
    page.get_by_text("Program").click()
    expect(page.get_by_role("alert")).not_to_be_visible()
    
    page.get_by_text("Administrative Office").click()
    expect(page.get_by_role("alert")).not_to_be_visible()
    
    page.get_by_text("Industry").click()
    expect(page.get_by_role("alert")).not_to_be_visible()
    
    page.get_by_text("Club").click()
    expect(page.get_by_role("alert")).not_to_be_visible()
    
    page.get_by_text("Research Institute").click()
    expect(page.get_by_role("alert")).not_to_be_visible()
    
    page.get_by_text("Startup").click()
    expect(page.get_by_role("alert")).not_to_be_visible()
    
    page.get_by_text("Patent Agency(Attorney)").click()
    expect(page.get_by_role("alert")).not_to_be_visible()
    
    page.locator("a").filter(has_text="Fundings").click()
    page.get_by_placeholder("Search...").click()
    page.get_by_placeholder("Search...").fill("test")
    page.get_by_placeholder("Search...").press("Enter")
    expect(page.get_by_role("alert")).not_to_be_visible()
    
    page.locator("p").filter(has_text="Draft").click()
    expect(page.get_by_role("alert")).not_to_be_visible()
    
    page.get_by_text("Pending").click()
    expect(page.get_by_role("alert")).not_to_be_visible()
    
    page.get_by_text("Active").click()
    expect(page.get_by_role("alert")).not_to_be_visible()
    
    page.get_by_text("Completed").click()
    expect(page.get_by_role("alert")).not_to_be_visible()
    
    page.get_by_text("Expired").click()
    expect(page.get_by_role("alert")).not_to_be_visible()
    
    page.get_by_text("Terminated").click()
    expect(page.get_by_role("alert")).not_to_be_visible()
    
    page.get_by_text("Others").click()
    expect(page.get_by_role("alert")).not_to_be_visible()