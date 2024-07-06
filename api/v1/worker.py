#!/usr/bin/python3
"""a module that handler background work"""
from models.crawler import Crawler
from models import storage
from models.products import Product
import asyncio


def job():
    """a function that handles job"""
    crawler = Crawler()
    products = crawler.parse('https://www.jumia.com.ng', '')
    if len(products) > 0:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(crawler.download_images_async(products))
        for product in products:
            product.save()
            description, specification = crawler.selected(product)
            description.save()
            specification.save()


def empty_storage():
    """a function that empty product storage"""
    storage.empty(Product)
