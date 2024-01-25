import os

from playwright.sync_api import Playwright, sync_playwright, expect
import pytest


@pytest.mark.regression
@pytest.mark.storefront
@pytest.mark.parametrize("email", ["rubellemari@gmail.com",
                                             pytest.param("rubellemari@gmail", marks=pytest.mark.xfail),
                                             pytest.param("fakeemail", marks=pytest.mark.xfail)])
@pytest.mark.parametrize("password", [os.environ ["PASSWORD"],
                                             pytest.param("fakepassword", marks=pytest.mark.xfail)])

def test_log_in(set_up, email, password) -> None:
    page = set_up
    newsletter_popup = page.locator(".newsletter-popup__content > div").first
    newsletter_popup.wait_for()
    page.locator(".absolute > .cursor-pointer > g > line:nth-child(2)").click()
    page.get_by_label("Go to my account").first.click()
    page.get_by_placeholder("Enter email address").fill(email)
    page.get_by_placeholder("Enter password").fill(password)
    page.get_by_role("button", name="Login").click()
    expect(page.get_by_role("link", name="Logout")).to_be_visible(timeout=6000)
    expect(page.get_by_text("rubellemari@gmail.com")).to_be_visible()
    expect(page.get_by_role("heading", name="Orders", exact=True)).to_be_visible()
    print('Login test PASSED')