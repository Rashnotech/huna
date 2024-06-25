#!/usr/bin/env python3
"""(main) entry for the ecommerce application"""
from bs4 import BeautifulSoup
from crawler import Crawler
from model.products import Product


crawler = Crawler()
products = crawler.parse('https://www.jumia.com.ng', '')
if products is not None and len(products) > 0:
    for product in products:
        crawler.download_images(product)