# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
import re

class BookscraperItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    pass

class ProductItem(scrapy.Item):
    url = scrapy.Field()
    product_name = scrapy.Field()
    product_price = scrapy.Field()
