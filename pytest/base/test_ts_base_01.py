"""
TS-BASE-01: verify user login function
@Author: Lingze
"""

import pytest
import re
from playwright.sync_api import Page, expect
from utils import AccountInfo
from utils.setting import InventorAccount, ManagerAccount


@pytest.mark.parametrize("role", ["inventor", "manager"])
def test_base_ts01_tc01(homepage:Page, role:str) -> None:
    """
    login successfully
    role : 'inventor' or 'manager'
    details refer to the test doc
    """
    page = homepage
    expect(page.get_by_role("link", name="Home")).to_be_visible()
    expect(page.get_by_role("link", name="Inventions")).to_be_visible()
    expect(page.get_by_role("link", name="Settings")).to_be_visible()

    if role == "manager":
        expect(page.get_by_role("link", name="Patents")).to_be_visible()
        expect(page.get_by_role("link", name="Events")).to_be_visible()
        expect(page.get_by_role("link", name="Organizations")).to_be_visible()
        expect(page.get_by_role("link", name="Fundings")).to_be_visible()
        expect(page.get_by_role("link", name="Demands")).to_be_visible()
        expect(page.get_by_role("link", name="Agreements")).to_be_visible()
        expect(page.get_by_role("link", name="IP8 Tech Manager")).to_be_visible()
        expect(page.get_by_role("link", name="Dashboard")).to_be_visible()
        expect(page.get_by_role("link", name="Users")).to_be_visible()


def test_base_ts01_tc02(base_page: Page) -> None:
    """
    login account is invalid
    details refer to the test doc
    """
    page = base_page 
    page.get_by_placeholder("Email address*").click()
    page.get_by_placeholder("Email address*").fill("invalida account")
    page.get_by_placeholder("Email address*").press("Tab")
    page.get_by_placeholder("Password*").fill("123456")
    page.get_by_role("button", name="Login").click()
    expect(page.get_by_text("Please provide a valid email")).to_be_visible()
    
def test_base_ts01_tc03(base_page: Page) -> None:
    """
    password is incorrect
    details refer to the test doc
    """
    page = base_page
    page.get_by_placeholder("Email address*").click()
    page.get_by_placeholder("Email address*").fill(InventorAccount.email)
    page.get_by_placeholder("Password*").click()
    page.get_by_placeholder("Password*").fill("1234")
    page.get_by_role("button", name="Login").click()
    expect(page.get_by_role("alert")).to_be_visible()

@pytest.mark.parametrize("role", ["inventor", "manager"])
def test_base_ts01_tc05(homepage:Page, role:str) -> None:
    """
    logout successfully
    """
    page = homepage
    page.get_by_text("l", exact=True).click()
    page.locator("div").filter(has_text=re.compile(r"^Logout$")).nth(1).click()
    expect(page.get_by_text("Login").first).to_be_visible()
    expect(page.get_by_role("button", name="Login")).to_be_visible()
    