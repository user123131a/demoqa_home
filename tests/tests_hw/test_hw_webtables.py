from pages.webtables import WebTables
import time


def test_webtables(browser):
    webtables = WebTables(browser)
    webtables.visit()

    # удаляем все записи из таблицы , затем проверяем No rows found
    while webtables.btn_delete_row.exist():
        webtables.btn_delete_row.click()
    time.sleep(2)
    assert webtables.no_data.exist()

    # проверка, что диалоговое окно закрыто
    assert not webtables.modal_backdrop.exist()
    time.sleep(2)

    # кликаем, затем проверка, что диалоговое окно открыто
    webtables.btn_add.click()
    assert webtables.modal_backdrop.exist()
    time.sleep(2)

    # проверка того, что в диалоге нельзя сохранить пустую форму и окно не закрывается
    webtables.btn_modal_submit.click()
    assert webtables.modal_backdrop.exist() and webtables.user_form.get_dom_attribute('class') == 'was-validated'
    time.sleep(2)

    # заполняем поля и нажимаем сабмит
    webtables.first_name.send_keys('tester')
    webtables.last_name.send_keys('testerovich')
    webtables.email.send_keys('AAAA@asad.com')
    webtables.age.send_keys('25')
    webtables.salary.send_keys('123')
    webtables.department.send_keys('department')
    webtables.btn_modal_submit.click()
    time.sleep(2)

    # проверяем, что окно закрылось и что таблица не пуста
    assert not webtables.modal_backdrop.exist()
    assert not webtables.no_data.exist()

    # проверяем, что после нажатия на карандаш снова открывается форма
    webtables.pencil.click()
    assert webtables.modal_backdrop.exist()
    time.sleep(2)
    webtables.btn_modal_submit.click()

    #проверяем, что имя в таблице то, которое ранее указывали
    assert webtables.first_name_in_table.get_text() == 'tester'
    time.sleep(2)

    # f. если изменить имя и сохранить, то в таблице обновятся данные
    webtables.pencil.click()
    assert webtables.modal_backdrop.exist()
    webtables.first_name.send_keys('tester222')
    webtables.btn_modal_submit.click()
    assert webtables.first_name_in_table.get_text() == 'testertester222'
    time.sleep(2)

    # удаляем все записи из таблицы , затем проверяем No rows found
    while webtables.btn_delete_row.exist():
        webtables.btn_delete_row.click()
    time.sleep(2)
    assert webtables.no_data.exist()

#________________________________________________________________________________


def test_webtables_2(browser):
    webtables = WebTables(browser)
    webtables.visit() # страница открыта

    # переключаем таблицу на 5 строк
    webtables.rows.scroll_to_element()
    webtables.rows.click()
    webtables.btn_rows_5.click()
    time.sleep(2)

    assert webtables.pencil.check_count_elements(3)     # изначально строк 3, что сейчас проверили,
    webtables.drop() # добавляем еще 2, заполняем поля и нажимаем сабмит, функция описана в баз_пейдж
    webtables.drop()
    assert webtables.pencil.check_count_elements(5)     # проверяем что строк 5, по наличию иконки карандаша
    # проверяем, что кнопки Next и Previous заблокированы (имеют атрибут класса disabled)
    assert webtables.btn_next.get_dom_attribute('disabled') == ''
    assert webtables.btn_previous.get_dom_attribute('disabled') == ''
    time.sleep(2)
    webtables.drop() # добавляем еще 3 строки
    webtables.drop()
    webtables.drop()
    time.sleep(2)
    assert webtables.btn_next.click()
    assert webtables.pencil.check_count_elements(3)  # на второй странице 3 строки
    assert webtables.btn_next.get_dom_attribute('disabled') == ''
    assert webtables.btn_previous.get_dom_attribute('class') == '-btn'
    time.sleep(2)
    assert webtables.btn_previous.click()
    assert webtables.pencil.check_count_elements(5)  # на первой странице 5 строк
    assert webtables.btn_next.get_dom_attribute('class') == '-btn'
    assert webtables.btn_previous.get_dom_attribute('disabled') == ''
    time.sleep(2)
