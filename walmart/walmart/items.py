# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WalmartItem(scrapy.Item):
    # define the fields for your item here like:
    # store = scrapy.Field()
    barcode = scrapy.Field()
    sku = scrapy.Field()
    brand = scrapy.Field()
    name = scrapy.Field()
    description = scrapy.Field()
    package = scrapy.Field()
    image_URL = scrapy.Field()
    # category = scrapy.Field()
    # URL = scrapy.Field()
    price = scrapy.Field()
    # stock = scrapy.Field()
    branch = scrapy.Field()
    
