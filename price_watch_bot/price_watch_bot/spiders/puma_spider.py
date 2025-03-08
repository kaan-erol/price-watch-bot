import scrapy
from price_watch_bot.items import ProductItem

class PumaSpiderSpider(scrapy.Spider):
    name = "puma_spider"
    allowed_domains = ["tr.puma.com"]
    start_urls = ["https://tr.puma.com/tifosi-unisex-ayakkabi-397454-05.html"]

    def parse(self, response):
        item = ProductItem()

        item['url'] = response.url
        item['product_name'] = response.xpath('//h1[@class="page-title"]/text()').get()
        item['product_price'] = response.xpath('//span[@class="price"]/text()').get()

        yield item
