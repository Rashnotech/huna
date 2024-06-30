#!/usr/bin/env python3
"""a module that crawls ecommerce sites"""
import requests
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
from urllib.parse import urlparse
from model.products import Product
from model.desc import Description
from model.specs import Specification
import re
import os


def rename(product) -> str:
    """utility function for renaming image files
    """
    rename = product.image_url.split('/')[-1]
    code = rename.split('?')[1]
    rename = rename.split('?')[0]
    name = code + rename
    return name


def currency(price) -> float:
    """convert price to amount"""
    amount = price.split('-')[0].strip(' ')
    new_price = amount[2:].replace(',', '')
    return float(new_price)


class Crawler:
    """
    A class to crawl and extract data from ecommerce websites.
    """
    directory = 'downloaded'
    visited = set()

    def get_page(self, url):
        """
        The function `get_page` sends a GET request to a specified
        URL and returns the parsed HTML content using BeautifulSoup.

        :param url: The `url` parameter represents the URL of the web
            page that you want to retrieve
        :return: a BeautifulSoup object created from the HTML content
            of the requested page.
        """
        try:
            session = requests.Session()
            headers = {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5)'
                'AppleWebKit 537.36 (KHTML, like Gecko) Chrome',
                'Accept': 'text/html,application/xhtml+xml,application/xml;'
                'q=0.9,image/webp,*/*;q=0.8'
            }
            req = session.get(url, headers=headers)
            return BeautifulSoup(req.text, "html.parser")
        except requests.exceptions.RequestException:
            return None

    def get(self, url):
        bs = self.get_page(url)
        if bs is not None:
            return bs
        else:
            return None

    def filter(self, obj, tag, attr, value):
        try:
            products = obj.find_all(tag, {attr: value})
            return products
        except AttributeError:
            return ""

    def parse(self, url, search=''):
        """parsing logic based on the site structure"""
        bs = self.get_page(url + search)
        objs = []
        if bs is None:
            return None
        products = self.filter(bs, 'article', 'class', 'prd _box _hvr')
        for product in products:
            prd_name = product.find('div', {'class': 'name'}).get_text()
            price = product.find('div', {'class': 'prc'}).get_text()
            discount = product.find('div', {'class': 'bdg _dsct'})
            image_url = product.find('img', attrs={'data-src':
                                     re.compile('^(https|www)')})
            link = product.find('a', href=re.compile('^/*.*$')).attrs['href']
            objs.append(Product(name=prd_name,
                                price=currency(price),
                                discount=discount.get_text()
                                if discount is not None else discount,
                                img_url=image_url['data-src'],
                                link=link
                                ))
        return objs

    def next(self,  visited):
        pass

    def download_images(self, product):
        if not os.path.exists(self.directory):
            os.makedirs(self.directory)
        try:
            response = requests.get(product.image_url, stream=True)
            response.raise_for_status()
            filename = os.path.join(self.directory,
                                    f'{rename(product)}')
            with open(filename, 'wb') as out_file:
                for chunk in response.iter_content(chunk_size=8192):
                    out_file.write(chunk)
        except Exception as e:
            return ""

    def selected(self, product) -> tuple:
        url = '{}{}'.format(
                'https://www.jumia.com.ng',
                urlparse(product.link).path
            )
        bs = self.get(url)
        descs = self.description(bs)
        desc['product_id'] = product.id
        specs = self.get_specs(bs)
        specs['product_id'] = product.id
        return (Description(**descs), Specification(**specs))

    def description(self, obj):
        kwargs = {}
        all_desc = obj.find('div', 'card aim -mtm')
        title = all_desc.find('header', {'class': '-pvs -bb'}).find('h2').text
        kwargs['title'] = title
        desc = all_desc.find('div', {'class': 'markup -mhm -pvl -oxa -sc'}).get_text(separator='\n')
        kwargs['desc'] = desc
        return kwargs

    def get_specs(self, obj):
        kwargs = {}
        all_specs = obj.find('div', {'class': 'card aim -mtm'})
        for spec in all_specs:
            spec = spec.parent.next_sibling
            kwargs['features'] = spec
        return kwargs
        """
        all_specs = obj.find('div', {'class': 'row -pas'})
        specs = self.filter(all_specs, 'article', 'class', 'col8 -pvs')
        for spec in specs:
            title = spec.find('div', {'class': 'markup -pam'}).text
            features = ['\n'.join(feat.get_text())
                        for feat in spec.find_all('ul')]
            kwargs['title'] = title
            kwargs['features'] = features
        return kwargs
        """

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Crawler, cls).__new__(cls)
        return cls.instance
