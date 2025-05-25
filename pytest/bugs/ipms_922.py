



import pytest
import time
from playwright.sync_api import Page, expect


@pytest.mark.parametrize("role", ["inventor"])
def test_ipms_922_case_1(homepage: Page) -> None:
    """reproduce 922 
    add drop-down icon 
    
    (done)
    """

    page = homepage
    page.get_by_role("link", name="Inventions").click()
    page.get_by_role("link", name="Just Pick a Sign: Optimizing").click()
    page.get_by_role("button", name="Submit").click()
    expect(page.get_by_label("angle down")).to_be_visible()
    

@pytest.mark.parametrize("role", ["inventor"])
def test_ipms_922_case_2(homepage: Page) -> None:
    """
    """

    page = homepage
    page.get_by_role("link", name="Inventions").click()
    page.get_by_role("link", name="一种以自然语言搜索关系型复杂管理信息系统数据的方法及系统").click()
    page.get_by_role("button", name="Submit").click()
    expect(page.get_by_label("angle down")).to_be_visible()