# Price Watch Bot

A simple web scraping project to track product prices from various online stores. The bot scrapes product prices daily from **Puma** and **Nike** websites, stores the data in a MySQL database, and sends an email notification when the price drops.

---

## Features

- Scrapes product data from Puma and Nike websites.
- Stores product URLs, names, and prices in a MySQL database.
- Sends email notifications when a product goes on sale (price drops).
- Uses **Scrapy** for web scraping.
- Runs daily using **GitHub Actions**.

---

## Requirements

Before running the project, make sure you have the following installed:

- Python 3.9+  
- MySQL (or any MySQL-compatible database)
- Scrapy (install via `pip install scrapy`)
- smtplib (used for sending email notifications)

---

## Installation

### Clone the repository:

```bash
git clone https://github.com/kaan-erol/price-watch-bot.git 
```

### Install required dependencies:

```bash
pip install -r requirements.txt
```

### Configure your environment:

Create a config.py file and define your MySQL credentials and email settings:

```python
MYSQL_HOST = "your-mysql-host"
MYSQL_USER = "your-mysql-username"
MYSQL_PASSWORD = "your-mysql-password"
MYSQL_DATABASE = "your-mysql-database"

SENDER_EMAIL = "your-email@gmail.com"
RECEIVER_EMAIL = "receiver-email@example.com"
APP_PASSWORD = "your-app-password"
```

For email notifications, you can use your Gmail account. Generate an App Password if you have 2FA enabled on your Gmail account.

## Usage

### Run the Scrapy Spider:

You can run the Puma or Nike spider using the following commands:

```bash
scrapy crawl puma_spider
```

```bash
scrapy crawl nike_spider
```

### Email Notification:

The bot will automatically send an email notification when a product's price drops.

### Scheduling:

The scraping process runs daily on GitHub Actions, so no need to keep your computer on.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
