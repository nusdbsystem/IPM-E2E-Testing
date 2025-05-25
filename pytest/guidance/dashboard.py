
import pytest
import time
from playwright.sync_api import Page, expect
import re
from utils.setting import InventorAccount, ManagerAccount


@pytest.mark.parametrize("role", ["manager"])
def test_bashboard_case(homepage: Page) -> None:
    page = homepage
    page.locator("a").filter(has_text="Organization Dashboard").click()

    expect(page.get_by_text("Invention Distribution by Tag")).to_be_visible()
    expect(page.get_by_text("TRL Distribution by Invention")).to_be_visible()
    expect(page.get_by_text("CRL Distribution by Invention")).to_be_visible()

    expect(page.locator(
        "div:nth-child(10) > .MuiBox-root > .echarts-for-react > div > canvas")).to_be_visible()
    expect(page.locator(
        "div:nth-child(8) > .MuiBox-root > .echarts-for-react > div > canvas")).to_be_visible()
    expect(page.locator(
        "div:nth-child(7) > .MuiBox-root > .echarts-for-react > div > canvas")).to_be_visible()
    expect(page.locator(
        "div:nth-child(6) > .MuiBox-root > .echarts-for-react > div > canvas")).to_be_visible()
    expect(page.locator(
        ".MuiGrid-root > div:nth-child(5) > .MuiBox-root")).to_be_visible()
