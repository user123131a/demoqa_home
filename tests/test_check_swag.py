import requests
from pytest import fixture, mark

@fixture
def url():
    return "https://www.saucedemo.com/"

def test_icon(url):
    response = requests.get(url)
    assert response.status_code == 200
    # Проверить наличие иконки
    icon_element = response.content.find("<i class='fas fa-user'>")
    assert icon_element != -1

def test_name_field(url):
    response = requests.get(url)
    assert response.status_code == 200
    # Проверить наличие поля имени
    name_element = response.content.find("input[type='text']")
    assert name_element != -1

def test_password_field(url):
    response = requests.get(url)
    assert response.status_code == 200
    # Проверить наличие поля пароля
    password_element = response.content.find("input[type='password']")
    assert password_element != -1

