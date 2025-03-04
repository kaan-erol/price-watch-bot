# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

def serialize_price(value):
    return float(value.replace('₺', '').replace(',', '.').strip())

class ProductItem(scrapy.Item):
    url = scrapy.Field()
    product_name = scrapy.Field()
    product_price = scrapy.Field(serializer=serialize_price)
    brand = scrapy.Field()
