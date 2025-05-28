import pytest
from playwright.sync_api import Page
from utils.setting import InventorAccount, ManagerAccount, BaseUrl


def inventor_login(page: Page) -> None:
    """
    Login as an inventor
    """
    # page goto the login url
    page.goto(BaseUrl)

    page.get_by_placeholder("Email address*").click()
    page.get_by_placeholder("Email address*").fill(InventorAccount.email)
    page.get_by_placeholder("Password*").click()
    page.get_by_placeholder("Password*").fill(InventorAccount.password)
    page.get_by_role("button", name="Login").click()


def manager_login(page: Page) -> None:
    """
    Login as a manager
    """
    # page goto the login url
    page.goto(BaseUrl)

    page.get_by_placeholder("Email address*").click()
    page.get_by_placeholder("Email address*").fill(ManagerAccount.email)
    page.get_by_placeholder("Password*").click()
    page.get_by_placeholder("Password*").fill(ManagerAccount.password)
    page.get_by_role("button", name="Login").click()
