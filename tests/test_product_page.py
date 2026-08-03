import re
from pages.product_page import ProductPage


def test_add_product_to_cart(driver):
    """
    Verify that a product can be viewed and successfully added to the cart.
    """
    product_page = ProductPage(driver)
    product_page.open_products_page()
    product_page.view_product()
    assert "/product_details/1" in driver.current_url, \
        f"Expected to be on product details page, but URL was: {driver.current_url}"
    product_page.add_to_cart()
    assert product_page.product_is_added(), "Product was not confirmed as added to cart"


def test_product_details_displayed(driver):
    """
    Verify that the product name and price are correctly displayed
    on the product details page.
    """
    product_page = ProductPage(driver)
    product_page.open_products_page()
    product_page.view_product()
    assert "/product_details/1" in driver.current_url, \
        f"Expected to be on product details page, but URL was: {driver.current_url}"

    product_title = product_page.product_name_in_view_product().text
    assert product_title == "Blue Top", \
        f"Expected product title 'Blue Top', but got '{product_title}'"

    product_price_txt = product_page.product_price_in_view_product().text
    product_price = int(product_price_txt.replace("Rs. ", ""))
    assert product_price == 500, \
        f"Expected product price 500, but got {product_price}"


def test_product_details_for_multiple_products(driver):
    """
    Verify that product name and price are correctly displayed
    for several different products, not just the first one.
    """
    product_page = ProductPage(driver)
    product_page.open_products_page()

    expected_products = [
        (0, "Blue Top", 500),
        (1, "Men Tshirt", 400),
        (2, "Sleeveless Dress", 1000),
    ]

    for index, expected_name, expected_price in expected_products:
        product_page.open_products_page()  # vrati se na listu pre svakog proizvoda
        product_page.view_product_by_index(index)

        product_title = re.sub(r'\s+', ' ', product_page.product_name_in_view_product().text).strip()
        assert product_title == expected_name, \
            f"Expected '{expected_name}' at index {index}, but got '{product_title}'"

        product_price_txt = product_page.product_price_in_view_product().text
        product_price = int(product_price_txt.replace("Rs. ", ""))
        assert product_price == expected_price, \
            f"Expected price {expected_price} at index {index}, but got {product_price}"