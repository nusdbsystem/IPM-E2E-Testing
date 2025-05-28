import pytest
import time
from playwright.sync_api import Page, expect
import re
from utils.setting import InventorAccount, ManagerAccount
from utils.util import manager_login, inventor_login


@pytest.mark.parametrize("role", ["manager"])
def test_invention_case_manager(homepage: Page) -> None:
    page = homepage

    page.get_by_role("link", name="Inventions").click()
    page.get_by_role("button", name="Create").click()
    page.get_by_placeholder("Enter a title for this").click()
    page.get_by_placeholder("Enter a title for this").fill("Only For test")

    # choose template
    page.get_by_role("combobox").click()
    page.get_by_text("None").click()
    page.locator("span").filter(has_text="None").first.click()
    page.get_by_text("Default").dblclick()
    page.get_by_role("button", name="Create").click()

    # check this invention
    expect(page.get_by_text("Overview").nth(1)).to_be_visible()
    expect(page.get_by_role("button", name="Edit")).to_be_visible()
    expect(page.get_by_text("Invention ID")).to_be_visible()
    expect(page.get_by_text("Title")).to_be_visible()
    expect(page.get_by_text("Abstract", exact=True)).to_be_visible()
    expect(page.get_by_text("General Domain")).to_be_visible()
    expect(page.get_by_text("Tags", exact=True)).to_be_visible()
    expect(page.get_by_text("Technology Readiness Level (")).to_be_visible()
    expect(page.get_by_text("Commercial Readiness Level (")).to_be_visible()

    # chcek section
    page.get_by_role("link", name="Sections").click()
    expect(page.get_by_role("button", name="Generate Disclosure")).to_be_visible()
    expect(page.get_by_role("button", name="Generate Tech offer")).to_be_visible()
    expect(page.get_by_role("button", name="Reorder")).to_be_visible()
    expect(page.get_by_role("button", name="Add Section").first).to_be_visible()
    expect(page.get_by_text("Sections").nth(1)).to_be_visible()

    # delete
    page.locator("button").filter(has_text="Delete").click()
    expect(page.get_by_text("Delete Invention?")).to_be_visible()
    expect(page.get_by_role("button", name="Confirm")).to_be_visible()
    page.get_by_role("button", name="Confirm").click()

    # back to homepage
    expect(page.get_by_text("All Inventions").nth(1)).to_be_visible()


@pytest.mark.parametrize("role", ["inventor"])
def test_invention_case_inventor(homepage: Page) -> None:
    page = homepage
    ip_id = "Invention-ID-Test-Inventor-Create"
    title = "only for test title"
    page.locator("a").filter(has_text="Inventions").click()
    page.get_by_role("button", name="Create").click()
    page.get_by_placeholder("Enter a title for this").click()
    page.get_by_placeholder("Enter a title for this").fill(title)
    page.locator("span").filter(has_text="Default").first.click()
    page.get_by_text("None").click()
    page.get_by_role("button", name="Create").click()
    page.get_by_role("link", name="Sections").click()
    expect(page.get_by_role("button", name="Generate Disclosure")).to_be_visible()
    expect(page.get_by_role("button", name="Generate Tech offer")).to_be_visible()
    expect(page.get_by_role("button", name="Add Section").first).to_be_visible()

    page.get_by_role("link", name="Overview").click()
    page.get_by_role("button", name="Edit").click()
    page.get_by_role("textbox").first.click()
    page.get_by_role("textbox").first.fill(ip_id)
    page.get_by_role("textbox").nth(2).click()
    page.get_by_role("textbox").nth(2).fill("Abstract")

    page.get_by_label("angle down").click()
    page.get_by_role("treeitem", name="Aerospace & Marine Technology").locator(
        "span").first.click()
    page.get_by_label("angle up").click()
    page.get_by_role("option", name="Energy & Environmental").get_by_label(
        "angle right").click()
    page.get_by_role("option", name="Environmental Monitoring & Pollution Control").locator(
        "span").first.click()
    page.get_by_label("angle up").click()

    page.locator("div").filter(has_text=re.compile(
        r"^Technology Readiness Level \(TRL\)Calculate$")).get_by_role("button").click()
    page.locator("label").filter(has_text="Preliminary testing of").click()
    page.get_by_text("Actual product/system has").click()
    page.get_by_text("Mapping product/system").click()
    page.get_by_role("button", name="Calculate").click()
    page.locator("div").filter(has_text=re.compile(
        r"^Commercial Readiness Level \(CRL\)Calculate$")).get_by_role("button").click()
    page.get_by_text("The product/system has been").click()
    page.get_by_text("Full and complete").click()
    page.get_by_text("Market and customer/partner").click()
    page.locator("label").filter(
        has_text="Full scale manufacturing and").click()
    page.get_by_role("button", name="Calculate").click()
    page.get_by_role("button", name="Save").click()

    # go back to inventions
    page.get_by_role("link", name="Inventions").click()

    # search the new invention ip
    page.get_by_placeholder("Search...").fill(title)
    page.get_by_placeholder("Search...").press("Enter")

    # delete this new invention, locate by title
    page.get_by_text(title, exact=True).locator(
        "xpath=ancestor::div[3]").get_by_role("button").click()
    page.get_by_role("button", name="Confirm").click()


@pytest.mark.parametrize("role", ["manager"])
def test_manager_assign_ip_inventor(homepage: Page) -> None:
    """
    1. manager create a new IP
    2. manager assign an inventor to this IP
    3. inventor have access to this IP
    """

    page = homepage
    title = "IP for Team Coporation"

    page.get_by_role("link", name="Inventions").click()
    # manager create a empty IP
    page.get_by_role("button", name="Create").click()
    page.get_by_placeholder("Enter a title for this").click()
    page.get_by_placeholder("Enter a title for this").fill(title)
    page.get_by_role("button", name="Create").click()

    # to Advanced (Page)
    page.get_by_text("Advanced").click()

    # first remove the inventor, if exist
    tmp = page.get_by_role(
        "row", name=InventorAccount.email).get_by_role("button")
    if tmp.count() != 0:
        # already have this inventor, remove it first
        page.get_by_role("row", name=InventorAccount.email).get_by_role(
            "button").click()
        page.get_by_role("button", name="Confirm").click()

    # add inventors

    page.get_by_role("button", name="Add").first.click()
    page.locator("div").filter(has_text=re.compile(
        r"^Select inventor$")).nth(3).click()
    page.get_by_placeholder("Search").fill(InventorAccount.email)
    # page.get_by_text(f"{InventorAccount.email}", exact=True).click()
    page.get_by_role("searchbox").locator("xpath=ancestor::div[1]").get_by_text(
        f"{InventorAccount.email}", exact=True).click()
    page.get_by_role("button", name="Add").click()

    # assert the newly added inventor
    page.get_by_text(InventorAccount.email, exact=True).is_visible()

    # repeated add same inventor, should get error list
    page.get_by_role("button", name="Add").first.click()
    page.locator("div").filter(has_text=re.compile(
        r"^Select inventor$")).nth(3).click()
    page.get_by_placeholder("Search").fill(InventorAccount.email)
    page.get_by_role("searchbox").locator("xpath=ancestor::div[1]").get_by_text(
        f"{InventorAccount.email}", exact=True).click()
    page.get_by_role("button", name="Add").click()
    page.get_by_text("This inventor has already", exact=True).is_visible()

    # #----------- Inventor Part to Validate -----------
    # login inventor account
    inventor_login(page)
    page.get_by_role("link", name="Inventions").click()

    page.get_by_placeholder("Search...").fill(title)
    page.get_by_placeholder("Search...").press("Enter")

    ans = page.get_by_role("link", name=title, exact=True)
    assert ans.count() == 1, "The IP should be created by manager"

    # # --------------- Manager Delete this New Created IP -----------------
    # login manager account
    manager_login(page)
    page.get_by_role("link", name="Inventions").click()
    page.get_by_placeholder("Search...").fill(title)
    page.get_by_placeholder("Search...").press("Enter")
    page.get_by_role("link", name=title, exact=True).click()

    # delete the created ip
    page.get_by_role("button", name="Delete").click()
    page.get_by_role("button", name="Confirm").click()
