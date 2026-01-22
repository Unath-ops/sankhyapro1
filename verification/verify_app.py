from playwright.sync_api import Page, expect, sync_playwright

def verify_app(page: Page):
    # Navigate to the app
    page.goto("http://localhost:5173")

    # Check for the title or header
    # "SANKHYA" and "Let's Audit Your Karma." are in the header
    expect(page.get_by_text("SANKHYA")).to_be_visible()
    expect(page.get_by_text("Let's Audit Your Karma.")).to_be_visible()

    # Check for inputs
    expect(page.get_by_label("Your Name")).to_be_visible()

    # Take a screenshot
    page.screenshot(path="verification/sankhya_landing.png")

if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        try:
            verify_app(page)
        finally:
            browser.close()
