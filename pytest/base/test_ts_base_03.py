"""
TS-BASE-03: verify change profile function
"""
import pytest
from playwright.sync_api import Page, expect


@pytest.mark.parametrize("role", ["inventor", "manager"])
def test_base_ts03_tc_01(homepage: Page, role: str) -> None:
    """
    change profile function
    """
    page = homepage
    page.get_by_role("button", name="Edit profile").click()
    button = page.locator(
        "div:nth-child(4) > .MuiPaper-root > .MuiInputBase-root > .MuiInputBase-input")
    expect(button).to_be_disabled()