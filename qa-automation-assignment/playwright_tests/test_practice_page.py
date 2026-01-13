from playwright.sync_api import sync_playwright

def test_practice_page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://rahulshettyacademy.com/AutomationPractice/")

        page.check("#checkBoxOption1")
        page.select_option("#dropdown-class-example", "option2")
        page.fill("#name", "Neelam")
        page.click("#alertbtn")

        browser.close()