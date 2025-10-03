from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    chromium = playwright.chromium.launch(headless=False)
    page = chromium.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

    Email_input = page.locator('//div[@data-testid="login-form-email-input"]//div//input')
    Email_input.focus()

    for char in "user@gmail.com":
        page.keyboard.type(char, delay=300.)

    page.keyboard.press("ControlOrMeta+A")


    page.wait_for_timeout(5000)