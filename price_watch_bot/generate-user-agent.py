import random

browsers = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{version} Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{version} Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{version} Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:119.0) Gecko/20100101 Firefox/{version}",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Version/{version} Safari/537.36"
]

def random_version():
    major = random.randint(80, 120)
    minor = random.randint(0, 999)
    return f"{major}.{minor}.0.0"

def generate_user_agent():
    browser = random.choice(browsers)
    version = random_version()
    return browser.format(version=version)

num_agents = 100

with open("user_agents.txt", "w") as f:
    for _ in range(num_agents):
        f.write(generate_user_agent() + "\n")
