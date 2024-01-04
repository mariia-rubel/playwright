from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.lucypittaway.co.uk/")
    page.wait_for_load_state()
    page.locator(".absolute > .cursor-pointer > g > line:nth-child(2)").click()
    page.get_by_label("Go to my account").first.click()
    page.get_by_placeholder("Enter email address").click()
    page.get_by_placeholder("Enter email address").fill("rubellemari@gmail.com")
    page.get_by_placeholder("Enter password").click()
    page.get_by_placeholder("Enter password").fill("testtesttest123!")
    page.get_by_role("button", name="Login").click()
    print('Login test PASSED')
    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
