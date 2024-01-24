import os
from playwright.sync_api import Playwright, sync_playwright, expect


def test_upload_image(set_up_pdf) -> None:
    page = set_up_pdf
    cwd = os.getcwd()
    file_path = os.path.join(cwd, "testdata", "image.pdf")
    page.locator("xpath =//div[1]/button").nth(0).scroll_into_view_if_needed()
    with page.expect_file_chooser() as fc_info:
        page.locator("xpath =//div[1]/button").nth(0).click()
    file_chooser = fc_info.value
    file_chooser.set_files(file_path)
    page.wait_for_timeout(5000)
    page.get_by_role("button", name="Convert").click()
    successful_message = page.get_by_text("Task finished. The download")
    successful_message.wait_for(timeout = 50000)
    print("Upload Image PASSED")

    # ---------------------


