import pytest
import time
from playwright.sync_api import Page, expect


@pytest.mark.parametrize("role", ["manager"])
def test_ipms_926_bug_case_1(homepage: Page) -> None:
    """reproduce 926 bug
    mismatch between navigation bar
    """

    page = homepage
    page.get_by_role("link", name="Inventions").click()
    page.get_by_placeholder("Search...").click()
    page.get_by_placeholder("Search...").fill("Cool")
    page.locator(
        ".MuiStack-root > div > div > .MuiButtonBase-root").first.click()
    page.get_by_role("link", name="Cool: a COhort OnLine").click()
    page.get_by_text("Preliminary Valuation").click()
    page.go_back()

    # check the navigation bar
    # there is a mismatch in the conten and activated bar
    # time.sleep(10)



@pytest.mark.parametrize("role", ["manager"])
def test_ipms_926_bug_case_2(homepage: Page) -> None:
    """reproduce 926 bug
    mismatch between navigation bar
    
    (reproduce, not fixed)
    """

    page = homepage
    page.get_by_role("link", name="Inventions").click()
    page.get_by_placeholder("Search...").click()
    page.get_by_placeholder("Search...").fill("METER")
    page.locator(
        ".MuiStack-root > div > div > .MuiButtonBase-root").first.click()
    page.get_by_role("link", name="METER: A Dynamic Concept").click()
    page.get_by_text("Advanced").click()
    
    page.go_back()
    
    # time.sleep(10)



@pytest.mark.parametrize("role", ["manager"])
def test_ipms_926_bug_case_3(homepage: Page) -> None:
    """reproduce 926 bug
    mismatch between navigation bar
    """

    page = homepage
    page.get_by_role("link", name="Inventions").click()
    page.get_by_placeholder("Search...").click()
    page.get_by_placeholder("Search...").fill("AlphaEvolve")
    page.locator(".MuiStack-root > div > div > .MuiButtonBase-root").first.click()
    page.get_by_role("link", name="AlphaEvolve: A Learning").click()
    page.get_by_text("Advanced").click()
    page.get_by_role("link", name="Cost").click()
    page.go_back()
    page.go_back()
    # time.sleep(10)
