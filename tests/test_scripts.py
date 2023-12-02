import os.path
import time

from page_objects.Sbis_contacts import SbisContacts
from page_objects.Sbis import Sbis
from page_objects.Sbis_download import SbisDownload
from page_objects.Tenzor import Tenzor
from page_objects.Tenzor_about import TenzorAbout


def test_first_script(browser):
    # 1) Перейти на https://sbis.ru/ в раздел "Контакты"
    Sbis(browser).open_contacts()
    # 2) Найти баннер Тензор, кликнуть по нему
    SbisContacts(browser).open_tenzor()
    # 3) Перейти на https://tensor.ru/
    browser.switch_to.window(browser.window_handles[-1])
    # 4) Проверить, что есть блок "Сила в людях"
    block_power_in_people = Tenzor(browser).find_block_content()
    assert Tenzor(block_power_in_people).find_power_in_people() == 'Сила в людях'
    # 5) Перейдите в этом блоке в "Подробнее" и убедитесь, что открывается https://tensor.ru/about
    Tenzor(block_power_in_people).open_more()
    assert browser.current_url == 'https://tensor.ru/about'
    # 6) Находим раздел Работаем и проверяем, что у всех фотографии
    # хронологии одинаковые высота (height) и ширина (width)
    block_working = TenzorAbout(browser).find_working()
    images = TenzorAbout(block_working).get_images()
    first_image = images[0]
    for img in images[1:]:
        assert first_image.size['height'] == img.size['height']
        assert first_image.size['width'] == img.size['width']


def test_second_script(browser):
    # 1) Перейти на https://sbis.ru/ в раздел "Контакты"
    Sbis(browser).open_contacts()
    # 2) Проверить, что определился ваш регион и есть список партнеров.
    assert SbisContacts(browser).get_region().text == 'Республика Татарстан'
    partners_of_tatarstan = SbisContacts(browser).get_partners()
    assert len(SbisContacts(browser).get_partners()) > 0
    # 3) Изменить регион на Камчатский край
    SbisContacts(browser).open_region().open_kamchatka()
    # 4) Проверить, что подставился выбранный регион, список партнеров
    # изменился, url и title содержат информацию выбранного региона
    assert SbisContacts(browser).get_region().text == 'Камчатский край'
    assert SbisContacts(browser).get_partners() != partners_of_tatarstan
    assert '41-kamchatskij-kraj' in browser.current_url
    assert 'Камчатский край' in browser.title


def test_third_script(browser):
    # 1) Перейти на https://sbis.ru/
    Sbis(browser).open_page()
    # 2) В Footer'e найти и перейти "Скачать СБИС"
    Sbis(browser).download_sbis()
    # 3) Скачать СБИС Плагин для вашей для windows, веб-установщик в папку с данным тестом
    SbisDownload(browser).open_sbis_plagin().download_web()
    # 4) Убедиться, что плагин скачался
    assert os.path.exists('tests/sbisplugin-setup-web.exe')
    # 5) Сравнить размер скачанного файла в мегабайтах. Он должен
    # совпадать с указанным на сайте (в примере 3.64 МБ).
    assert round(os.path.getsize('tests/sbisplugin-setup-web.exe') / (1024 * 1024), 2) == 3.66
