from pages.cart_page import CartPage


def test_add_to_cart_and_verify_in_cart(driver):
    """
    Verify that a single product can be added to the cart and that
    the correct product name appears in the cart afterward.
    """
    cart_page = CartPage(driver)
    cart_page.open_products_page()
    cart_page.view_product()
    assert "/product_details/1" in driver.current_url, \
        f"Expected to be on product details page, but URL was: {driver.current_url}"
    cart_page.add_to_cart()
    assert cart_page.product_is_added(), "Product was not confirmed as added to cart"
    cart_page.view_cart()
    product_name = cart_page.product_name_in_cart()
    assert product_name == "Blue Top", \
        f"Expected 'Blue Top' in cart, but found '{product_name}'"


def test_remove_item_from_cart(driver):
    """
    Verify that a product added to the cart can be removed,
    and that the cart correctly shows the empty state afterward.
    """
    cart_page = CartPage(driver)
    cart_page.open_products_page()
    cart_page.view_product()
    assert "/product_details/1" in driver.current_url, \
        f"Expected to be on product details page, but URL was: {driver.current_url}"
    cart_page.add_to_cart()
    assert cart_page.product_is_added(), "Product was not confirmed as added to cart"
    cart_page.view_cart()
    product_name = cart_page.product_name_in_cart()
    assert product_name == "Blue Top", \
        f"Expected 'Blue Top' in cart, but found '{product_name}'"
    cart_page.remove_item_from_cart()
    message = cart_page.get_empty_cart_message()
    assert message == "Cart is empty!", \
        f"Expected empty cart message, but got: '{message}'"


def test_add_multiple_products_to_cart(driver):
    """
    Verify that multiple products can be added to the cart in a single flow
    using JS click as a workaround for ad overlay interception.
    """
    cart_page = CartPage(driver)
    cart_page.open_products_page()
    cart_page.add_multiple_products_to_cart([0, 1, 2])
    cart_page.view_cart_from_page()
    items_count = cart_page.get_cart_items_count()
    assert items_count == 3, \
        f"Expected 3 items in cart, but found {items_count}"


def test_ui_add_multiple_products_via_real_hover_and_click(driver):
    """
    Verify that multiple products can be added to the cart using real user
    interaction (ActionChains hover + click), and that all added items
    are distinct products with no duplicates.
    """
    cart_page = CartPage(driver)
    cart_page.open_products_page()
    for index in [0, 1, 2]:
        cart_page.add_product_to_cart_via_user_click(index)

    cart_page.view_cart_from_page()
    names_in_cart = cart_page.get_cart_item_names()

    assert len(names_in_cart) == 3, \
        f"Expected 3 items in cart, but found {len(names_in_cart)}: {names_in_cart}"
    assert len(set(names_in_cart)) == 3, \
        f"Expected 3 unique products, but found duplicates: {names_in_cart}"


def test_update_quantity_and_verify_total_price(driver):
    """
    Verify that updating product quantity before adding to cart correctly
    updates the cart quantity and recalculates the total price.
    """
    cart_page = CartPage(driver)
    cart_page.open_products_page()
    cart_page.view_product()
    view_price_str = cart_page.product_price_in_view_product().text
    view_price = int(view_price_str.replace("Rs. ", ""))
    assert view_price == 500, \
        f"Expected unit price 500, but found {view_price}"
    cart_page.set_quantity(3)
    cart_page.add_to_cart()
    assert cart_page.product_is_added(), "Product was not confirmed as added to cart"
    cart_page.view_cart()
    items_count = cart_page.get_cart_items_count()
    assert items_count == 1, \
        f"Expected 1 line item in cart, but found {items_count}"
    quantity = cart_page.cart_quantity()
    assert quantity == "3", \
        f"Expected quantity '3', but found '{quantity}'"
    total_price_text = cart_page.cart_product_price().text
    total_price = int(total_price_text.replace("Rs. ", ""))
    assert total_price == 500 * 3, \
        f"Expected total price {500*3}, but found {total_price}"