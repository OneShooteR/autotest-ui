from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    chromium = playwright.chromium.launch(headless=False)
    page = chromium.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

    email_input = page.locator('//div[@data-testid="login-form-email-input"]//div//input')
    email_input.fill('user.name@mail.com')
    password_input = page.locator('//input[@type="password"]')
    password_input.fill('password')

    password_input = page.locator('//button[@data-testid="login-page-login-button"]')
    password_input.click()

    wrong_email_or_password_alert = page.locator('//div[@data-testid="login-page-wrong-email-or-password-alert"]')
    expect(wrong_email_or_password_alert).to_be_visible()
    expect(wrong_email_or_password_alert).to_have_text("Wrong email or password")
    page.wait_for_timeout(5000)