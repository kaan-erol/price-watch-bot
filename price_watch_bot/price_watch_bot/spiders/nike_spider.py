import scrapy


class NikeSpiderSpider(scrapy.Spider):
    name = "nike_spider"
    allowed_domains = ["nike.com"]
    start_urls = ["https://nike.com"]

    def parse(self, response):
        pass
