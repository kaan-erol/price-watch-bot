import scrapy


class AdidasSpiderSpider(scrapy.Spider):
    name = "adidas_spider"
    allowed_domains = ["www.adidas.com.tr"]
    start_urls = ["https://www.adidas.com.tr/tr/samba-og-ayakkabi/B75806.html"]

    def parse(self, response):
        pass
