import scrapy


class AdidasSpiderSpider(scrapy.Spider):
    name = "adidas_spider"
    allowed_domains = ["adidas.com"]
    start_urls = ["https://adidas.com"]

    def parse(self, response):
        pass
