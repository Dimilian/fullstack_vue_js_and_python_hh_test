from typing import List, Dict
from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup


def _get_headers():
    headers = requests.utils.default_headers()
    headers.update({
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'
    })
    return headers


def _get_html_data(url: str, params=None) -> str:
    req = requests.get(url, params=params, headers=_get_headers())
    return req.content.decode('utf-8')


def _get_product_links(html: str, host: str) -> List[str]:
    """
    Получаем список ссылок на продукты с одной страницы
    """
    soup = BeautifulSoup(html, 'html.parser')
    a_elements = soup.select('.j-card-item .j-open-full-product-card')
    links_list = ['{0}{1}'.format(host, elem.get('href')) for elem in a_elements]
    return links_list


def _parse_products(links: List[str]) -> List[Dict[str, str]]:
    """
    Получаем всю информацию по продуктам из списка ссылок в виде списка словарей
    """
    print('Start parsing...\n')
    product_list = []
    for link in links:
        product_soup = BeautifulSoup(_get_html_data(link), 'html.parser')
        product_data = {}
        product_data = {
            'brand': getattr(product_soup.select_one('.j-product-title .brand'), 'text', None),
            'name': getattr(product_soup.select_one('.j-product-title .name'), 'text', None),
            'article': getattr(product_soup.select_one('.article span'), 'text', None),
            'rating': getattr(product_soup.select_one('.product-rating .rating span'), 'text', None),
            'actual_price': getattr(product_soup.select_one('.final-cost'), 'text', None),
            'composition': getattr(product_soup.select_one('.i-composition-v1 .j-consist'), 'text', None),
            'description': getattr(product_soup.select_one('.j-description'), 'text', None),
            'params': ','.join(['{0}:{1}'.format(p.select_one('span:nth-child(1)').text.strip(),
                                                 p.select_one('span:nth-child(2)').text.strip()) for p in
                                product_soup.select('.params .pp')])
        }
        product_list.append(product_data)
    return product_list


def _get_all_products_links(url) -> List[str]:
    """
    Получаем список ссылок на продукты в категории со всех страниц
    """
    page_num = 1
    page_exists = True
    all_links = []
    host = '{uri.scheme}://{uri.netloc}'.format(uri=urlparse(url))

    while page_exists:
        products_links = []
        products_list_html = _get_html_data(url, {'page': page_num})
        products_links = _get_product_links(products_list_html, host)
        if products_links:
            all_links.extend(products_links)
            page_num += 1
        else:
            print(
                'Общее количество страниц с товарами: {0}\n'
                'Общее количество товаров в категории: {1}'.format(
                    page_num - 1, len(all_links)
                )
            )
            page_exists = False

    return all_links


def get_products(category_url: str) -> List[Dict[str, str]]:
    products_links = _get_all_products_links(category_url)
    products_data_list = _parse_products(products_links)
    return products_data_list
