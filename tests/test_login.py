from pages.login_page import LoginPage


def test_login_with_valid_credentials(driver):
    """
    Verify that a user can successfully log in with valid credentials
    and that the logged-in username is displayed correctly.
    """
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("userovic1@gmail.com", "12345")

    logged_in_username = login_page.get_logged_in_username()
    assert "12345" in logged_in_username, \
        f"Expected '12345' in logged-in username, but got: '{logged_in_username}'"
    assert login_page.is_login_confirmed(), "Login was not confirmed after valid credentials"


def test_login_with_invalid_credentials(driver):
    """
    Verify that login fails with an incorrect password and that the
    user remains on the login page.
    """
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("userovic1@gmail.com", "1234")

    assert login_page.not_logged_in(), "User appears logged in despite invalid credentials"
    assert "login" in driver.current_url, \
        f"Expected to remain on login page, but URL was: {driver.current_url}"


def test_login_with_empty_password(driver):
    """
    Verify that login fails when the password field is left empty,
    keeping the user on the login page.
    """
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("userovic1@gmail.com", "")

    assert "login" in driver.current_url, \
        f"Expected to remain on login page with empty password, but URL was: {driver.current_url}"


def test_login_with_empty_email(driver):
    """
    Verify that login fails when the email field is left empty,
    keeping the user on the login page.
    """
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("", "12345")

    assert "login" in driver.current_url, \
        f"Expected to remain on login page with empty email, but URL was: {driver.current_url}"