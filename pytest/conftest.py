import pytest
from utils import AccountInfo
from typing import Generator

from playwright.sync_api import Page, sync_playwright


@pytest.fixture(scope='session')
def inventor_account() -> AccountInfo:
    return AccountInfo(email="lingze_v@ip8value.com", password="123")


@pytest.fixture(scope='session')
def manager_account() -> AccountInfo:
    return AccountInfo(email="lingze_m@ip8value.com", password="lingze")


@pytest.fixture(scope='session')
def browser_context():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        yield context
        context.close()
        browser.close()


@pytest.fixture(scope='function')
def base_page(browser_context) -> Generator[Page, None, None]:
    page = browser_context.new_page()
    page.goto("http://137.132.92.226:4001/login")
    yield page
    page.close()


@pytest.fixture(scope="function")
def inventor_homepage(base_page: Page, inventor_account: AccountInfo) -> Generator[Page, None, None]:
    base_page.get_by_placeholder("Email address*").click()
    base_page.get_by_placeholder("Email address*").fill(inventor_account.email)
    base_page.get_by_placeholder("Password*").click()
    base_page.get_by_placeholder("Password*").fill(inventor_account.password)
    base_page.get_by_role("button", name="Login").click()
    yield base_page


@pytest.fixture(scope="function")
def manager_homepage(base_page: Page, manager_account: AccountInfo):
    base_page.get_by_placeholder("Email address*").click()
    base_page.get_by_placeholder("Email address*").fill(manager_account.email)
    base_page.get_by_placeholder("Password*").click()
    base_page.get_by_placeholder("Password*").fill(manager_account.password)
    base_page.get_by_role("button", name="Login").click()
    yield base_page