import pytest
from utils import AccountInfo
from typing import Generator

from utils import setting 

from playwright.sync_api import Page, sync_playwright



@pytest.fixture(scope='session')
def browser_context():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        yield context
        context.close()
        browser.close()


@pytest.fixture(scope='function')
def base_page(browser_context) -> Generator[Page, None, None]:
    page = browser_context.new_page()
    page.goto(setting.BaseUrl)
    yield page
    page.close()    
    
@pytest.fixture(scope="function")
def homepage(base_page: Page, role:str) -> Generator[Page, None, None]:
    if role == "inventor":
        account:AccountInfo = setting.InventorAccount
    elif role == "manager":
        account:AccountInfo = setting.ManagerAccount
    
    base_page.get_by_placeholder("Email address*").click()
    base_page.get_by_placeholder("Email address*").fill(account.email)
    base_page.get_by_placeholder("Password*").click()
    base_page.get_by_placeholder("Password*").fill(account.password)
    base_page.get_by_role("button", name="Login").click()
    yield base_page