import pytest
import time
from playwright.sync_api import Page, expect



@pytest.mark.parametrize("role", ["inventor", "manager"])
def test_ipms_927_bug(homepage: Page) -> None:
    """reproduce 927 bug
    automatically log out when page back
    """
    
    page = homepage
    page.get_by_role("link", name="Inventions").click()
    
    page.locator()
    time.sleep(10)
    