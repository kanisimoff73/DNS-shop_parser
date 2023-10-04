from selenium import webdriver
from time import sleep


def get_qrator_key():
    """
    Функция, которая получает ключ qrator_jsid, чтобы в дальнейшем можно было парсить сайт при помощи скрипта
    Так как получение ключа происходи при помощи библиотеки selenium первое, что нужно сделать это добавить
    опцию отключения детекта хром-драйвера, после чего инициализировать драйвер нашего браузера и удалить некоторые
    методы у объекта window.
    """
    print("Получаем 'qrator_jsid', пожалуйста ждите.")
    options = webdriver.ChromeOptions()
    options.add_argument(
        'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 '
        'Safari/537.36'
    )  # добавим user agent нашего браузера
    options.add_argument("--disable-blink-features=AutomationControlled")  # опция отключения детекта хром-драйвера
    options.add_argument("--headless")  # метод для запуска браузера в фоновом режиме

    driver = webdriver.Chrome(options=options)  # инициализация драйвера
    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        'source': '''
    delete window.cdc_adoQpoasnfa76pfcZLmcfl_Array;
    delete window.cdc_adoQpoasnfa76pfcZLmcfl_Promise;
    delete window.cdc_adoQpoasnfa76pfcZLmcfl_Symbol;
    '''
    })

    try:
        driver.get(url='https://www.dns-shop.ru/')
        sleep(3)  # для того, чтобы браузер успел прогрузиться
        qrator_jsid = driver.get_cookie('qrator_jsid')['value']
        print("'qrator_jsid' получен, начинаем процесс сбора данных. Пожалуйста, подождите.")
        return qrator_jsid
    except Exception as ex:
        print("Не удалось получить 'qrator_jsid'")
        raise ex
    finally:
        driver.close()
        driver.quit()
