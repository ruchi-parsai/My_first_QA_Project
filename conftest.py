import pytest
from playwright.sync_api import sync_playwright

BASE_URL = "https://opensource-demo.orangehrmlive.com/"

@pytest.fixture(scope="function")
def page():
    with sync_playwright() as p:
        # browser = p.chromium.launch(headless=False)
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        page.goto(BASE_URL, wait_until="domcontentloaded", timeout=60000)
        # page.goto(BASE_URL, timeout=120000)
        yield page
        context.close()
        browser.close()








