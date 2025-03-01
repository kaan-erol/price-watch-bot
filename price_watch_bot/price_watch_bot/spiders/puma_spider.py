import scrapy


class PumaSpiderSpider(scrapy.Spider):
    name = "puma_spider"
    allowed_domains = ["puma.com"]
    start_urls = ["https://puma.com"]

    def parse(self, response):
        pass
