import time
from pages.window_tab import WindowTab


def test_window_tab(browser):
    page_window = WindowTab(browser)
    page_window.visit()
    time.sleep(2)
    assert page_window.lnk_home.exist()
    assert page_window.lnk_home.get_text() == "Home"
    assert page_window.lnk_home.get_dom_attribute('href') == "https://demoqa.com"
    time.sleep(2)

    assert len(browser.window_handles) == 1 # проверка списка открытых вкладок
    page_window.lnk_home.click()
    time.sleep(2)
    assert len(browser.window_handles) == 2
