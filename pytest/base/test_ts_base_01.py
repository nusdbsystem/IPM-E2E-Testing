"""
TS-BASE-01: verify user login function
@ Author: Lingze
"""

import re
from playwright.sync_api import Page, expect
from utils import AccountInfo

def test_tc_01(base_page: Page, inventor_account:AccountInfo) -> None:
    """
    inventor login successfully
    details refer to the test doc
    """
    page = base_page
    # page.goto("http://137.132.92.226:4001/login")
    page.get_by_placeholder("Email address*").click()
    page.get_by_placeholder("Email address*").fill(inventor_account.email)
    page.get_by_placeholder("Password*").click()
    page.get_by_placeholder("Password*").fill(inventor_account.password)
    page.get_by_role("button", name="Login").click()
    expect(page.get_by_role("link", name="Home")).to_be_visible()
    expect(page.get_by_role("link", name="Inventions")).to_be_visible()
    expect(page.get_by_role("link", name="Settings")).to_be_visible()



def test_tc_02(base_page: Page) -> None:
    """
    login account is invalid
    details refer to the test doc
    """
    page = base_page 
    # page.goto("http://137.132.92.226:4001/login")
    page.get_by_placeholder("Email address*").click()
    page.get_by_placeholder("Email address*").fill("invalida account")
    page.get_by_placeholder("Email address*").press("Tab")
    page.get_by_placeholder("Password*").fill("123456")
    page.get_by_role("button", name="Login").click()
    expect(page.get_by_text("Please provide a valid email")).to_be_visible()
    

def test_tc_03(base_page: Page) -> None:
    """
    password is incorrect
    details refer to the test doc
    """
    page = base_page
    page.get_by_placeholder("Email address*").click()
    page.get_by_placeholder("Email address*").fill("lingze_v@ip8value.com")
    page.get_by_placeholder("Password*").click()
    page.get_by_placeholder("Password*").fill("1234")
    page.get_by_role("button", name="Login").click()
    expect(page.get_by_role("alert")).to_be_visible()



def test_tc_04(base_page: Page) -> None:
    """
    manager account login successfully
    details refer to the test doc
    """
    page = base_page
    page.get_by_placeholder("Email address*").click()
    page.get_by_placeholder("Email address*").fill("lingze_m@ip8value.com")
    page.get_by_placeholder("Password*").click()
    page.get_by_placeholder("Password*").fill("lingze")
    page.get_by_role("button", name="Login").click()
    expect(page.get_by_role("link", name="Home")).to_be_visible()
    expect(page.get_by_role("link", name="Inventions")).to_be_visible()
    expect(page.get_by_role("link", name="Patents")).to_be_visible()
    expect(page.get_by_role("link", name="Events")).to_be_visible()
    expect(page.get_by_role("link", name="Organizations")).to_be_visible()
    expect(page.get_by_role("link", name="Fundings")).to_be_visible()
    expect(page.get_by_role("link", name="Demands")).to_be_visible()
    expect(page.get_by_role("link", name="Agreements")).to_be_visible()
    expect(page.get_by_role("link", name="IP8 Tech Manager")).to_be_visible()
    expect(page.get_by_role("link", name="Dashboard")).to_be_visible()
    expect(page.get_by_role("link", name="Settings")).to_be_visible()
    expect(page.get_by_role("link", name="Users")).to_be_visible()
    
    


def test_tc_05(inventor_homepage:Page) -> None:
    """
    logout successfully
    """
    page = inventor_homepage
    page.get_by_text("l", exact=True).click()
    page.locator("div").filter(has_text=re.compile(r"^Logout$")).nth(1).click()
    expect(page.get_by_text("Login").first).to_be_visible()
    expect(page.get_by_role("button", name="Login")).to_be_visible()
    