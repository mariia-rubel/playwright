from playwright.sync_api import Playwright, sync_playwright, expect

'''
Go to stationary > PDP of 'Sycamore Gap A5 Notebook', add the item to Cart and verify that the correct data 
displayed in the Cart widget. Then remove the item from the Cart widget and verify that the Cart widget closed and 
there are no items in the Cart.

'''
def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.lucypittaway.co.uk/")
    page.locator(".absolute > .cursor-pointer").click()
    page.get_by_role("link", name="Stationery", exact=True).click()
    page.get_by_role("link", name="Sycamore Gap A5 Notebook").click()
    page.get_by_role("button", name="View your cart add to basket").click()
    page.wait_for_load_state("networkidle")
    expect(page.locator("xpath=//p").nth(1)).to_have_text('Basket (1)', timeout=7000)
    expect(page.get_by_role("link", name="Sycamore Gap A5 Notebook")).to_be_visible()
    expect(page.get_by_text("Qty: 1")).to_be_visible()
    expect(page.locator("#cart-preview").get_by_role("img", name="Sycamore Gap A5 Notebook")).to_be_visible()
    expect(page.get_by_role("cell", name="Total (excluding delivery)")).to_be_visible()
    expect(page.locator('xpath=//td').nth(5)).not_to_be_empty()
    expect(page.get_by_role("link", name="Checkout")).to_be_enabled()
    expect(page.get_by_role("link", name="View Basket")).to_be_enabled()
    page.get_by_role("button", name="Remove").click()
    page.wait_for_load_state("networkidle")
    expect(page.locator("xpath=//a[3]/div")).not_to_be_visible()
    print('Add to Cart test PASSED')

with sync_playwright() as playwright:
    run(playwright)
