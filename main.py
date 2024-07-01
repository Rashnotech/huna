#!/usr/bin/env python3
"""(main) entry for the ecommerce application"""
from bs4 import BeautifulSoup
from crawler import Crawler
from model.products import Product
from schedule import every, repeat
import time


crawler = Crawler()
products = crawler.parse('https://www.jumia.com.ng', '')
if products is not None and len(products) > 0:
    for product in products:
        product.save()
        desc, specs = crawler.selected(product)
        crawler.download_images(product)
        desc.save()
        specs.save()
