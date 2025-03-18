from pages.modal_dialogs import Modal_dialogs
from conftest import browser
def test_modal_elements(browser):
    modal = Modal_dialogs(browser)
    modal.visit()
    assert modal.modal.check_count_elements(5)


def test_navigation_modal():
    # Открыть браузер и перейти на страницу https://demoqa.com/modal-dialogs
    browser = webdriver.Chrome()
    browser.get("https://demoqa.com/modal-dialogs")

    # Обновить страницу
    browser.refresh()

    # Перейти на главную страницу через иконку
    icon = browser.find_element_by_xpath("//a[@href='/']")
    icon.click()

    # Сделать шаг назад стрелкой браузера
    browser.action.back()

    # Установить размеры экрана 900х400
    browser.set_window_size(900, 400)

    # Сделать шаг вперед стрелкой браузера
    browser.action.forward()

    # Проверить URL главной страницы
    assert browser.current_url == "https://demoqa.com/"

    # Проверить title главной страницы
    title = browser.title
    assert title == "Demo QA | Free Online Testing Tool"

    # Вернуть размеры экрана по умолчанию 1000x1000
    browser.maximize_window()
    sleep(2)  # Дать время браузеру изменить размер окна

    # Закрыть браузер
    browser.quit()

if __name__ == "__main__":
    test_navigation_modal()
