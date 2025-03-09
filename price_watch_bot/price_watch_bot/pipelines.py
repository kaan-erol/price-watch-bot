# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import mysql.connector
from config import MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DATABASE

class PriceWatchBotPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)

        price_keys = ['product_price']
        for price_key in price_keys:
            value = adapter.get(price_key)
            value = value.replace('₺', '')
            value = value.replace('.', '')
            value = value.replace(',', '.')
            adapter[price_key] = float(value)

        return item

class SaveToMySQLPipeline:
    
    def __init__(self):
        self.conn = mysql.connector.connect(
            host=MYSQL_HOST,
            user=MYSQL_USER,
            password=MYSQL_PASSWORD,
            database=MYSQL_DATABASE
        )

        self.cur = self.conn.cursor()

        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INT NOT NULL AUTO_INCREMENT,
            url VARCHAR(255),
            product_name TEXT,
            product_price DECIMAL,
            PRIMARY KEY (id)
        )
        """)

    def process_item(self, item, spider):
        self.cur.execute(""" INSERT INTO products (
            url,
            product_name,
            product_price
            ) VALUES (
                %s, 
                %s, 
                %s
            ) """, (
            item["url"],
            item["product_name"],
            item["product_price"]
        ))

        self.conn.commit()
        return item
    
    def close_spider(self, spider):
        self.cur.close()
        self.conn.close()
