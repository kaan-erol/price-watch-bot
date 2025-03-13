import scrapy
from price_watch_bot.items import ProductItem
import mysql.connector
from price_watch_bot.config import MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DATABASE

class PumaSpiderSpider(scrapy.Spider):
    name = "puma_spider"
    allowed_domains = ["tr.puma.com"]

    def __init__(self):
        # Initialize database connection when the spider starts.
        self.conn = mysql.connector.connect(
            host=MYSQL_HOST,
            user=MYSQL_USER,
            password=MYSQL_PASSWORD,
            database=MYSQL_DATABASE
        )
        self.cur = self.conn.cursor()

    def start_requests(self):
        # Fetch product URLs from the database and start scraping each one.
        self.cur.execute("SELECT url FROM products")
        urls = self.cur.fetchall()
        
        for url in urls:
            yield scrapy.Request(url=url[0], callback=self.parse)

    def parse(self, response):
        # Extract product details
        item = ProductItem()

        item['url'] = response.url
        item['product_name'] = response.xpath('//h1[@class="page-title"]/text()').get()
        item['product_price'] = response.xpath('//span[@class="price"]/text()').get()

        yield item

    def close_spider(self, spider):
        # Close database connection
        self.cur.close()
        self.conn.close()