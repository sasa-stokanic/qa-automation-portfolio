from pages.register_page import RegisterPage


def test_register_page_happy_path(driver):
    """
    Verify the full registration flow: create a new account with all
    required fields, confirm account creation, then delete the account.
    """
    register_page = RegisterPage(driver)
    register_page.open()
    register_page.register("user1", "user1966@gmail.com")
    register_page.select_gender()
    register_page.enter_name_password("User", "12345")
    register_page.select_birth_day("29", "March", "1996")
    register_page.enter_user_info(
        "User", "Userovic", "Paunova59", "Ne znam", "Belgrade", "11000", "1111111")
    register_page.create_account()

    assert register_page.account_created(), "Account creation confirmation was not displayed"

    register_page.continue_button()
    register_page.delete_account()

    assert register_page.account_deleted(), "Account deletion confirmation was not displayed"


def test_register_with_existing_email(driver):
    """
    Verify that attempting to register with an email address that
    already exists on the site shows the appropriate error message.
    """
    register_page = RegisterPage(driver)
    register_page.open()
    register_page.register("useran", "userovic1@gmail.com")

    assert register_page.sign_up_existing_email(), \
        "Expected 'Email Address already exist!' message, but it was not displayed"


def test_register_with_empty_name(driver):
    """
    Verify that attempting to register with an empty name field
    keeps the user on the login/signup page instead of proceeding.
    """
    register_page = RegisterPage(driver)
    register_page.open()
    register_page.register("", "userovic1@gmail.com")

    assert "/signup" not in driver.current_url, \
        f"Expected registration to not proceed with empty name, but URL was: {driver.current_url}"
    

def test_register_with_empty_name_email(driver):
    """
    Verify that attempting to register with both name and email fields
    empty keeps the user on the login/signup page instead of proceeding.
    """
    register_page = RegisterPage(driver)
    register_page.open()
    register_page.register("", "")

    assert "/signup" not in driver.current_url, \
        f"Expected registration to not proceed with empty name and email, but URL was: {driver.current_url}"
    

