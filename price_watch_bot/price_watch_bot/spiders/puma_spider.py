import scrapy


class PumaSpiderSpider(scrapy.Spider):
    name = "puma_spider"
    allowed_domains = ["tr.puma.com"]
    start_urls = ["https://tr.puma.com"]

    def parse(self, response):
        pass
