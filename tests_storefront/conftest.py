import pytest
import playwright
from playwright.sync_api import Playwright


@pytest.fixture()
def set_up (page):
    # context = browser.new_context()
    # page = context.new_page()
    page.goto("https://www.lucypittaway.co.uk/")
    page.set_default_timeout(15000)

    yield page

@pytest.fixture()
def set_up_pdf(playwright: Playwright):
    browser = (playwright.firefox.launch(headless=False))
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://online2pdf.com/")
    page.set_default_timeout(15000)

    yield page
