from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    chromium = playwright.chromium.launch(headless=False)
    page = chromium.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    Email_input = page.locator('//div[@data-testid="registration-form-email-input"]//input')
    Email_input.fill('user.name@gmail.com')

    Username_input = page.locator('//div[@data-testid="registration-form-username-input"]//input')
    Username_input.fill('username')

    password_input = page.locator('//div[@data-testid="registration-form-password-input"]//input')
    password_input.fill('password')

    Registration_input = page.locator('//button[@data-testid="registration-page-registration-button"]')
    Registration_input.click()

    dashboard = page.locator('//h6[@data-testid="dashboard-toolbar-title-text"]')
    expect(dashboard).to_have_text("Dashboard")
    page.wait_for_timeout(5000)

