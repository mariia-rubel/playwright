import pytest

@pytest.fixture()
def set_up (page):
    # context = browser.new_context()
    # page = context.new_page()
    page.goto("https://www.lucypittaway.co.uk/")
    page.set_default_timeout(15000)

    yield page
