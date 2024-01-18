from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:

    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context()
    page = context.new_page()
    page.set_default_timeout(15000)
    page.goto("https://www.lucypittaway.co.uk/")
    newsletter_popup = page.locator(".newsletter-popup__content > div").first
    newsletter_popup.wait_for()
    page.locator(".absolute > .cursor-pointer > g > line:nth-child(2)").click()
    page.get_by_label("Go to my account").first.click()
    page.get_by_placeholder("Enter email address").fill("rubellemari@gmail.com")
    page.get_by_placeholder("Enter password").fill("testtesttest123!")
    page.get_by_role("button", name="Login").click()
    expect(page.get_by_role("link", name="Logout")).to_be_visible(timeout=6000)
    expect(page.get_by_text("rubellemari@gmail.com")).to_be_visible()
    expect(page.get_by_role("heading", name="Orders", exact=True)).to_be_visible()
    print('Login test PASSED')



with sync_playwright() as playwright:
    run(playwright)
