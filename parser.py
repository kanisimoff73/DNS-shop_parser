import os
from time import sleep
import requests
import curl
from qrator_jsid import get_qrator_key
from bs4 import BeautifulSoup
import openpyxl


def page_request(url, cookies, params=None):
    """Функция выполняет запрос HTML-страницы, для дальнейшей работы с ней"""
    response = requests.get(url, cookies=cookies, params=params, headers=curl.headers)
    if response.status_code != 200:
        qrator_jsid = get_qrator_key()
        cookies = {
            '_csrf': curl.cookies['_csrf'],
            'qrator_jsid': qrator_jsid,
        }
        response = requests.get(url, cookies=cookies, params=params, headers=curl.headers)
    sleep(1)
    return response, cookies


def get_retail_rocket_product(data, cookies=None):
    """Функция выполняет запрос на получение словаря 'retail-rocket-product/' из него мы будем получать основную
    информацию о продуктах"""
    response = requests.post(
        'https://www.dns-shop.ru/ajax-state/retail-rocket-product/',
        cookies=cookies,
        headers=curl.headers_retail_rocket_product,
        data=data
    )
    if response.status_code != 200:
        qrator_jsid = get_qrator_key()
        cookies = {
            '_csrf': curl.cookies['_csrf'],
            'qrator_jsid': qrator_jsid,
        }
        response = requests.post(
            'https://www.dns-shop.ru/ajax-state/retail-rocket-product/',
            cookies=cookies,
            headers=curl.headers_retail_rocket_product,
            data=data
        )
    sleep(1)
    return response, cookies


def save_links_to_products(soup):
    """Функция собирает ссылки на продукты, которые есть в категории каталога"""
    links_to_products = []
    links = soup.find_all('a', {'class': 'catalog-product__name'})
    for link in links:
        links_to_products.append(link.get('href'))
    return links_to_products


def save_the_product_category(category, qrator_jsid, cookies):
    """Основная функция, которая получает категорию в каталоге и проходиться по всем её продуктам используя функцию
    'save_links_to_products()'"""
    list_of_products = []

    if not qrator_jsid:
        qrator_jsid = get_qrator_key()
        cookies = {
            '_csrf': curl.cookies['_csrf'],
            'qrator_jsid': qrator_jsid,
        }

    params = {
        'stock': 'now-out_of_stock',  # определяет товары, которые есть в наличии
    }

    response, cookies = page_request(category, cookies=cookies, params=params)

    soup = BeautifulSoup(response.text, "lxml")
    category = soup.find('div', {'class': 'products-page__title'}).find('h1').text
    list_of_products.extend(save_links_to_products(soup))
    last_page = soup.find('a', {'class': 'pagination-widget__page-link_last'})
    if last_page:
        total_number_of_pages = int(
            soup.find('a', {'class': 'pagination-widget__page-link_last'}).get('href').split('=')[-1])
        if total_number_of_pages > 1:
            # Проходимся по всем страницам и записываем с них url товаров
            for page in range(2, total_number_of_pages + 1):
                params = {
                    'stock': 'now-out_of_stock',
                    'p': f'{page}',
                }
                response, cookies = page_request(category, cookies=cookies, params=params)
                soup = BeautifulSoup(response.text, "lxml")
                list_of_products.extend(save_links_to_products(soup))
    return list_of_products, cookies, category


def get_product_information(url, cookies):
    """2-я основная функция, которая получает всю информацию о продукте"""
    link = f'https://www.dns-shop.ru{url}characteristics/'
    response, cookies = page_request(link, cookies=cookies)
    soup = BeautifulSoup(response.text, 'lxml')
    characteristics = dict(
        zip((char.text.strip() for char in soup.find_all('div', {'class': 'product-characteristics__spec-title'})),
            (char.text.strip() for char in soup.find_all('div', {'class': 'product-characteristics__spec-value'}))))
    product = soup.find('div', {'class': 'product-card'}).get('data-product-card').strip()
    scripts = soup.find_all('script')
    for script in scripts:
        if '"type":"retail-rocket-product"' in script.text:
            product_id = script.text.split('"type":"retail-rocket-product"')[1][10:19]
    for script in scripts:
        if 'window.initProductImagesSlider' in script.text:
            dict_list = eval(script.text.split(',"has3d"', 1)[0].split('"images":')[1])
            links_to_photos = []
            for el in dict_list:
                links_to_photos.append(el['desktop'].replace('\\', ''))

    data = f'data={{"type":"retail-rocket-product","containers":[{{"id":"{product_id}","data":{{"product":"{product}","requestUrl":"{url}"}}}}]}}'
    response, cookies = get_retail_rocket_product(data=data, cookies=cookies)
    json_res = response.json()['data']['states'][0]['data']['data']
    price = json_res['price']
    main_image = json_res['pictureUrl']
    available = json_res['isAvailable']
    description = json_res['description']
    name = json_res['name']
    total_data = {
        'name': name,
        'price': price,
        'available': available,
        'link': link,
        'main_image': main_image,
        'links_to_photos': links_to_photos,
        'characteristics': characteristics,
        'description': description,
    }
    return total_data, cookies


def create_excel():
    """
    Создаём excel файл если его нет или если он создан более 24ч назад и заполняем,
    иначе возвращаем существующий файл
    """
    if not os.path.exists('statistics.xlsx'):
        workbook = openpyxl.Workbook()
        workbook.save('statistics.xlsx')

        category_links = ['https://www.dns-shop.ru/catalog/54d638e7f4d84e77/-/',
                          'https://www.dns-shop.ru/catalog/f5006471d2d49eac/razvetviteli-dlya-ventilyatorov/',
                          'https://www.dns-shop.ru/catalog/70f4b323b7c95d54/krepleniya-dlya-konsolej/',
                          'https://www.dns-shop.ru/catalog/recipe/ac636baae806e596/dozatory-dla-zubnoj-pasty/',
                          'https://www.dns-shop.ru/catalog/d41702130de56479/vstraivaemye-vinnye-shkafy/',
                          ]

        qrator_jsid = get_qrator_key()
        cookies = {
            '_csrf': curl.cookies['_csrf'],
            'qrator_jsid': qrator_jsid,
            'city_path': 'barnaul',
        }

        for category in category_links:
            list_of_products, cookies, category = save_the_product_category(category, qrator_jsid, cookies=cookies)
            title_to_excel = [
                'Категория',
                'Наименование',
                'Цена',
                'В наличии',
                'Ссылка страницы с товаром',
                'Ссылка на главное изображение',
                'Ссылки на все изображения',
                'Характеристики',
                'Описание'
            ]
            workbook.create_sheet(category)
            worksheet = workbook[category]
            worksheet.append(title_to_excel)
            workbook.save('statistics.xlsx')

            for url in list_of_products:
                try:
                    total_data, cookies = get_product_information(url, cookies=cookies)
                except Exception as e:
                    print(e)
                else:
                    data = [category, total_data['name'], total_data['price'], str(total_data['available']),
                            total_data['link'], total_data['main_image'], str(total_data['links_to_photos']),
                            str(total_data['characteristics']), total_data['description']]
                    worksheet = workbook[category]
                    worksheet.append(data)
                    workbook.save('statistics.xlsx')
                    workbook.close()
    return


if __name__ == '__main__':
    create_excel()
