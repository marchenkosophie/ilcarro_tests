from pages.login_page import LoginPage

VALID_EMAIL = "margo@gmail.com"
VALID_PASSWORD = "Mmar123456$"
INVALID_EMAIL = "wrong_user@gmail.com"


def test_login_success(driver):
    login_page = LoginPage(driver)


    login_page.open_login_form()
    login_page.fill_email(VALID_EMAIL)
    login_page.fill_password(VALID_PASSWORD)
    login_page.submit_login()

    assert login_page.login_success_text() == "You are logged in success"
    login_page.close_window()
    assert login_page.is_logged() == True




def test_login_success_1(driver):
    login_page = LoginPage(driver)

    login_page.open_login_form()
    login_page.login(VALID_EMAIL, VALID_PASSWORD)
    assert login_page.login_success_text() == "You are logged in success"
    login_page.close_window()
    assert login_page.is_logged() == True


def test_login_wrong_email(driver):
    login_page = LoginPage(driver)

    login_page.open_login_form()
    login_page.login(INVALID_EMAIL, VALID_PASSWORD)
    assert login_page.is_not_logged() == True



def test_login_wrong_password(driver):
    login_page = LoginPage(driver)

    login_page.open_login_form()
    login_page.login(INVALID_EMAIL, "123456")
    assert login_page.is_not_logged() == True


def test_login_unregistered_user(driver):
    login_page = LoginPage(driver)

    login_page.open_login_form()
    login_page.login("sophie@gmail.com", "Qwerty123")
    assert login_page.is_not_logged() == True


def test_login_invalid_email_format(driver):
    login_page = LoginPage(driver)

    login_page.open_login_form()
    login_page.fill_email("margogmail.com")
    login_page.fill_password(VALID_PASSWORD)

    assert login_page.is_submit_button_enabled() == False


def test_login_invalid_password_format(driver):
    login_page = LoginPage(driver)

    login_page.open_login_form()
    login_page.fill_email("margo@gmail.com")
    login_page.fill_password("")

    assert login_page.is_submit_button_enabled() == False
