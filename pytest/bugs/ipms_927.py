import pytest
import time
from playwright.sync_api import Page, expect



@pytest.mark.parametrize("role", ["inventor", "manager"])
def test_ipms_927_bug(homepage: Page) -> None:
    """reproduce 927 bug
    automatically log out when page back
    
    (reproduce, not fixed)
    """
    
    page = homepage
    page.goto("http://137.132.92.226:4001/error")
    expect(page.get_by_role("button", name="Return Home")).to_be_visible()
    expect(page.get_by_text("Something went wrong...")).to_be_visible()
    expect(page.get_by_text("We are unable to find the")).to_be_visible()
    page.get_by_role("button", name="Return Home").click()
    expect(page.get_by_text("Something went wrong...")).to_be_visible()
    expect(page.get_by_text("We are unable to find the")).to_be_visible()
    expect(page.get_by_role("button", name="Return Home")).to_be_visible()
    page.get_by_role("button", name="Return Home").click()
    expect(page.get_by_text("Login").first).to_be_visible()
    expect(page.get_by_role("button", name="Login")).to_be_visible()
    expect(page.get_by_text("Forgot password?")).to_be_visible()
    
    page.locator()
    time.sleep(10)
    