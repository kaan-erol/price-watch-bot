import scrapy
from price_watch_bot.items import ProductItem

class NikeSpiderSpider(scrapy.Spider):
    name = "nike_spider"
    allowed_domains = ["www.nike.com"]
    start_urls = ["https://www.nike.com/tr/t/dunk-low-retro-ayakkab%C4%B1s%C4%B1-mhrtZC/DD1391-103"]

    def parse(self, response):
        item = ProductItem()

        item['url'] = response.url
        item['product_name'] = response.xpath('//h1[@id="pdp_product_title"]/text()').get()
        item['product_price'] = response.xpath('//span[@data-testid="currentPrice-container"]/text()').get()

        yield item
