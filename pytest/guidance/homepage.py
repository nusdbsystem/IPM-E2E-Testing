import pytest
import time
from playwright.sync_api import Page, expect
import re
from utils.setting import InventorAccount, ManagerAccount


@pytest.mark.parametrize("role", ["manager"])
def test_homepage_case_manager(homepage: Page) -> None:
    page = homepage
    expect(page.get_by_text(ManagerAccount.email, exact=True)).to_be_visible()
    expect(page.get_by_role("button", name="Edit profile")).to_be_visible()

    expect(page.get_by_text(
        "Patent Distribution by Country", exact=True)).to_be_visible()
    expect(page.get_by_text(
        "Patent Distribution by Type", exact=True)).to_be_visible()
    expect(page.get_by_text(
        "TRL Distribution by Invention", exact=True)).to_be_visible()
    expect(page.get_by_text(
        "CRL Distribution by Invention", exact=True)).to_be_visible()

    expect(page.locator("div").filter(has_text=re.compile(
        r"^Last Modified Inventions$"))).to_be_visible()
    expect(page.locator("div").filter(has_text=re.compile(
        r"^Events \(Inventions\)$"))).to_be_visible()
    expect(page.locator("div").filter(has_text=re.compile(
        r"^Events \(Patents\)$"))).to_be_visible()
    expect(page.locator("div").filter(has_text=re.compile(
        r"^Events \(Agreements\)$"))).to_be_visible()

    expect(page.locator(".MuiStack-root > div").first).to_be_visible()
    expect(page.locator(
        "div:nth-child(2) > div:nth-child(5) > div:nth-child(2)")).to_be_visible()


@pytest.mark.parametrize("role", ["inventor"])
def test_homepage_case_inventor(homepage: Page) -> None:
    page = homepage
    # account
    expect(page.get_by_text(InventorAccount.email, exact=True)).to_be_visible()
    expect(page.get_by_text("About")).to_be_visible()
    expect(page.get_by_role("button", name="Edit profile")).to_be_visible()
    expect(page.get_by_text("Inventions").nth(1)).to_be_visible()
    expect(page.get_by_text(
        "Invention Distribution by Tag", exact=True)).to_be_visible()
    expect(page.get_by_text(
        "TRL Distribution by Invention", exact=True)).to_be_visible()
    expect(page.get_by_text(
        "CRL Distribution by Invention", exact=True)).to_be_visible()
    expect(page.locator("div").filter(has_text=re.compile(
        r"^Last Modified Inventions$"))).to_be_visible()
