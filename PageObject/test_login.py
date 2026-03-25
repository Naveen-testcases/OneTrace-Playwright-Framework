import re
from playwright.sync_api import Playwright,Page , expect


def test_run(page: Page):
   
    page.goto("https://dev.onetrace.com.au/")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("textbox", name="Email Address").click()
    page.get_by_role("textbox", name="Email Address").fill("pasupuletinaveenkumar22@gmail.com")
    page.get_by_role("textbox", name="Password").click()
    page.get_by_role("textbox", name="Password").fill("Test@123")
    page.get_by_role("checkbox", name="I accept to One Trace's Terms").check()
    page.get_by_role("button", name="Login").click()
    page.get_by_role("button", name="Create New Entry").click()
    page.get_by_role("button", name="Component Repair").click()
    page.get_by_role("textbox").nth(1).click()
    page.get_by_role("textbox").nth(1).fill("Sn-312333")
    page.get_by_role("textbox").nth(2).click()
    page.get_by_role("textbox").nth(2).fill("PON-312333")
    page.get_by_role("textbox").nth(3).click()
    page.get_by_role("textbox").nth(3).fill("Testing")
    page.get_by_role("textbox", name="Add Your Comments Here").click()
    page.get_by_role("textbox", name="Add Your Comments Here").fill("testing 76543")
    page.get_by_text("Select Enterprise").click()
    page.get_by_text("Ontrace SignOff2", exact=True).click()
    page.get_by_role("button", name="Select File Type Dropdown").click()
    page.get_by_role("button", name="Purchase order").click()
    page.get_by_text("Browse files").click()
    page.locator("body").set_input_files("export (7).csv")
    page.get_by_role("button", name="Submit").click()
    page.goto("https://dev.onetrace.com.au/tracing-dashboard")
    expect(page.locator("span").filter(has_text="PO# PON-")).to_be_visible()

   


