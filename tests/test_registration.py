# import random
import uuid

from models.user import User
from pages.registration_page import RegistrationPage


def test_registration_success(driver):
    registration_page = RegistrationPage(driver)
    # random_suffix = random.randint(1, 1_000_000)

    random_suffix = uuid.uuid4().hex[:8]
    user = User(
        "Tonny",
        "Molly",
        f"tony_{random_suffix}@gmail.com",
        "Password11$"
    )

    registration_page.open_registration_form()
    registration_page.fill_registration_form(user)
    registration_page.check_policy()
    registration_page.submit_registration()

    assert registration_page.confirmation_text() == "Registered"
    assert registration_page.confirmation_text_1() == "You are logged in success"

    registration_page.close_window()


def test_registration_with_empty_name(driver):
    registration_page = RegistrationPage(driver)

    user = User(
        "",
        "Molly",
        f"tony@gmail.com",
        "Password11$"
    )

    registration_page.open_registration_form()
    registration_page.fill_registration_form(user)
    registration_page.check_policy()
    registration_page.submit_registration()

    assert registration_page.error_message_text() == "Name is required"
    assert registration_page.submit_button_disabled()


def test_registration_with_empty_last_name(driver):
    registration_page = RegistrationPage(driver)

    user = User(
        "Tony",
        "",
        f"tony@gmail.com",
        "Password11$"
    )

    registration_page.open_registration_form()
    registration_page.fill_registration_form(user)
    registration_page.check_policy()
    registration_page.submit_registration()

    assert registration_page.error_message_text() == "Last name is required"
    assert registration_page.submit_button_disabled()


def test_registration_with_empty_email(driver):
    registration_page = RegistrationPage(driver)

    user = User(
        "Tony",
        "Molly",
        f"",
        "Password11$"
    )

    registration_page.open_registration_form()
    registration_page.fill_registration_form(user)
    registration_page.check_policy()
    registration_page.submit_registration()

    assert registration_page.error_message_text() == "Email is required"
    assert registration_page.submit_button_disabled()


def test_registration_with_wrong_password(driver):
    registration_page = RegistrationPage(driver)

    user = User(
        "Tony",
        "Molly",
        f"tony@gmail.com",
        "P1$"
    )

    registration_page.open_registration_form()
    registration_page.fill_registration_form(user)
    registration_page.check_policy()
    registration_page.submit_registration()

    assert registration_page.error_message_text() == "Password must contain minimum 6 symbols"
    assert registration_page.submit_button_disabled()


def test_registration_with_empty_password(driver):
    registration_page = RegistrationPage(driver)

    user = User(
        "Tony",
        "Molly",
        f"tony@gmail.com",
        ""
    )

    registration_page.open_registration_form()
    registration_page.fill_registration_form(user)
    registration_page.check_policy()
    registration_page.submit_registration()

    assert registration_page.error_message_text() == "Password is required"
    assert registration_page.submit_button_disabled()


def test_registration_without_check_box(driver):
    registration_page = RegistrationPage(driver)

    user = User(
        "Tony",
        "Molly",
        f"tony@gmail.com",
        "Password123$"
    )

    registration_page.open_registration_form()
    registration_page.fill_registration_form(user)
    registration_page.check_policy()
    registration_page.check_policy()
    registration_page.submit_registration()


    assert registration_page.error_message_text() == "You must accept the terms"
    assert registration_page.submit_button_disabled()


