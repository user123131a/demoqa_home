import time
from pages.alerts import Alerts

def test_alert(browser):
    alert_page = Alerts(browser)

    alert_page.visit()
    assert not alert_page.alert() # проверяем что алерта нет

    alert_page.timer_alertButton.click() # нажимаем на кнопку по локатору
    time.sleep(5)
    assert alert_page.alert()  # проверяем что алерт появился
    alert_page.alert().accept() # принимаем элемент и смотрим что нет активных элементов
    assert not alert_page.alert()
