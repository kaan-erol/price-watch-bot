# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sys
sys.path.append('C:/Users/kaane/Repository/price-watch-bot/price_watch_bot/price_watch_bot')
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
            url VARCHAR(255) UNIQUE,
            product_name TEXT,
            product_price DECIMAL,
            PRIMARY KEY (id)
        )
        """)

    def process_item(self, item, spider):
        self.cur.execute("SELECT product_price FROM products WHERE url = %s", (item["url"],))
        result = self.cur.fetchone()
        if result:
            old_price = result[0]
            # Fiyat düştüyse güncelle
            if item["product_price"] < old_price:
                self.cur.execute("""
                    UPDATE products
                    SET product_price = %s, product_name = %s
                    WHERE url = %s
                """, (item["product_price"], item["product_name"], item["url"]))
                print(f"Price dropped! The new price for {item['product_name']} has been updated.")
        else:
            # Eğer ürün yoksa ekle
            self.cur.execute("""
                INSERT INTO products (url, product_name, product_price)
                VALUES (%s, %s, %s)
            """, (item["url"], item["product_name"], item["product_price"]))
        self.conn.commit()
        return item
    
    def close_spider(self, spider):
        self.cur.close()
        self.conn.close()
