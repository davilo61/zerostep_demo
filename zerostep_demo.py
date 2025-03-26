import time
from playwright.sync_api import sync_playwright

def test_saucedemo_add_to_cart():
    """
    Test that logs into saucedemo.com and adds a product to the cart using Playwright.
    
    Installation:
    - pip install playwright
    - playwright install
    """
    with sync_playwright() as p:
        # Launch browser
        browser = p.chromium.launch(headless=False)  # Set headless=True for production
        context = browser.new_context()
        page = context.new_page()
        
        try:
            # Navigate to saucedemo.com
            page.goto("https://www.saucedemo.com")
            
            # Login with standard credentials
            page.fill("#user-name", "standard_user")
            page.fill("#password", "secret_sauce")
            page.click("#login-button")
            
            # Verify login was successful
            assert page.is_visible(".title"), "Products page not loaded"
            
            # Add a product to cart
            page.click("#add-to-cart-sauce-labs-backpack")
            
            # Verify product was added to cart
            page.click(".shopping_cart_link")
            assert page.is_visible(".inventory_item_name"), "Product not visible in cart"
            
            # Verify cart badge shows 1
            assert page.text_content(".shopping_cart_badge") == "1", "Cart count incorrect"
            
            # Proceed to checkout
            page.click("#checkout")
            
            # Fill checkout information
            page.fill("#first-name", "Test")
            page.fill("#last-name", "User")
            page.fill("#postal-code", "12345")
            
            # Continue to checkout overview
            page.click("#continue")
            
            # Verify checkout overview page loaded
            assert page.is_visible(".summary_info"), "Checkout overview not loaded"
            
            # Complete checkout
            page.click("#finish")
            
            # Verify order completion
            assert page.is_visible(".complete-header"), "Order not completed"
            assert "Thank you" in page.text_content(".complete-header"), "Completion message not found"
            
            # Check for the complete message text
            complete_text = page.text_content(".complete-text")
            assert "Your order has been dispatched" in complete_text, "Dispatch confirmation message not found"
            print(f"Complete message verified: '{complete_text}'")
            
            # Verify we're on the complete.html page
            assert "checkout-complete.html" in page.url, "Not on complete.html page"
            
            # Click the "Back Home" button
            page.click("#back-to-products")
            
            # Verify we're back on the home/inventory page
            assert "inventory.html" in page.url, "Not redirected to inventory page"
            assert page.is_visible(".inventory_container"), "Inventory container not visible"
            assert page.is_visible(".title"), "Products title not visible"
            assert page.text_content(".title") == "Products", "Products title not found"
            
            print("Successfully returned to home page after checkout")
            
            print("Test passed successfully! Checkout completed.")
            
            # Keep browser open for a moment to see the results
            time.sleep(3)
            
        finally:
            # Clean up
            context.close()
            browser.close()

if __name__ == "__main__":
    test_saucedemo_add_to_cart()