from pages.checkout_page import CheckoutPage


def test_checkout_flow(driver):
    """
    Verify the full checkout flow: login, add a product to cart,
    proceed to checkout, and confirm that the product name and price
    remain consistent between the cart and the checkout page.
    """
    checkout_page = CheckoutPage(driver)
    checkout_page.open_login_page()
    checkout_page.login("userovic1@gmail.com", "12345")
    checkout_page.login_confirmation()

    logged_in_text = checkout_page.login_confirmation()
    assert "User12345" in logged_in_text, \
        f"Expected 'User12345' in logged-in text, but got: '{logged_in_text}'"

    checkout_page.close_add_if_present()
    checkout_page.open_product_page()
    checkout_page.open_view_product()
    checkout_page.add_to_cart_in_product_view()
    checkout_page.view_cart()

    cart_items_count = checkout_page.product_in_cart_confirmation()
    assert cart_items_count == 1, \
        f"Expected 1 item in cart, but found {cart_items_count}"

    name_in_cart = checkout_page.take_product_name_in_cart()
    price_in_cart = checkout_page.take_product_price_in_cart()

    checkout_page.checkout_button_click()
    assert "/checkout" in driver.current_url, \
        f"Expected to be on checkout page, but URL was: {driver.current_url}"

    name_in_checkout = checkout_page.take_product_name_in_checkout()
    price_in_checkout = checkout_page.take_product_price_in_checkout()

    assert name_in_cart == name_in_checkout, \
        f"Product name mismatch: cart had '{name_in_cart}', checkout had '{name_in_checkout}'"
    assert price_in_cart == price_in_checkout, \
        f"Product price mismatch: cart had '{price_in_cart}', checkout had '{price_in_checkout}'"