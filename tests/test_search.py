from pages.search_page import SearchPage


def test_products_exist_after_search(driver):
    """
    Verify that searching for an existing product term ("dress")
    returns at least one matching product.
    """
    search_page = SearchPage(driver)
    search_page.open()
    search_page.search_input()
    search_page.search_button_click()
    search_page.wait_for_url()
    products = search_page.get_products()

    assert len(products) > 0, "Expected at least one product for 'dress' search, but found none"
    assert search_page.driver.current_url == SearchPage.SEARCH_DRESS_URL, \
        f"Expected URL '{SearchPage.SEARCH_DRESS_URL}', but got '{search_page.driver.current_url}'"


def test_empty_search(driver):
    """
    Verify the site's behavior when searching with an empty search term
    (currently returns all products rather than an empty result set).
    """
    search_page = SearchPage(driver)
    search_page.open()
    search_page.empty_search_input()
    search_page.search_button_click()
    search_page.wait_for_url()
    products = search_page.get_products()

    assert len(products) > 0, \
        f"Expected products to be returned for empty search, but found {len(products)}"
    assert search_page.driver.current_url == SearchPage.EMPTY_SEARCH_URL, \
        f"Expected URL '{SearchPage.EMPTY_SEARCH_URL}', but got '{search_page.driver.current_url}'"


def test_no_results_search(driver):
    """
    Verify that searching for a non-existing product term ("MotorBike")
    returns no results.
    """
    search_page = SearchPage(driver)
    search_page.open()
    search_page.non_existing_product_search()
    search_page.search_button_click()
    search_page.wait_for_url()
    products = search_page.get_products(wait_for_results=False)

    assert len(products) == 0, \
        f"Expected 0 products for 'MotorBike' search, but found {len(products)}"
    assert search_page.driver.current_url == SearchPage.MOTOR_BIKE_URL, \
        f"Expected URL '{SearchPage.MOTOR_BIKE_URL}', but got '{search_page.driver.current_url}'"
    