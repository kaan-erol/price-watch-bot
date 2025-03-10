import scrapy
from price_watch_bot.items import ProductItem
import mysql.connector
import sys
sys.path.append('C:/Users/kaane/Repository/price-watch-bot/price_watch_bot/price_watch_bot')
from config import MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DATABASE

class PumaSpiderSpider(scrapy.Spider):
    name = "puma_spider"
    allowed_domains = ["tr.puma.com"]

    def start_requests(self):
        conn = mysql.connector.connect(
            host=MYSQL_HOST,
            user=MYSQL_USER,
            password=MYSQL_PASSWORD,
            database=MYSQL_DATABASE
        )
        cur = conn.cursor()

        cur.execute("SELECT url FROM products")
        urls = cur.fetchall()
        
        for url in urls:
            yield scrapy.Request(url=url[0], callback=self.parse)

        cur.close()
        conn.close()

    def parse(self, response):
        item = ProductItem()

        item['url'] = response.url
        item['product_name'] = response.xpath('//h1[@class="page-title"]/text()').get()
        item['product_price'] = response.xpath('//span[@class="price"]/text()').get()

        yield item
