import scrapy


class NikeSpiderSpider(scrapy.Spider):
    name = "nike_spider"
    allowed_domains = ["www.nike.com"]
    start_urls = ["https://www.nike.com/tr/t/dunk-low-retro-ayakkab%C4%B1s%C4%B1-mhrtZC/DD1391-103"]

    def parse(self, response):
        product_name = response.xpath('//h1/text()').get()
        product_price = response.xpath('//span[contains(@class, "price")]/text()').get()

        yield {
            'product_name': product_name,
            'product_price': product_price,
            'url': response.url,
        }
