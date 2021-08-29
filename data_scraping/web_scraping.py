import os
from icrawler.builtin import GoogleImageCrawler

os.mkdir('coke')
google_crawler = GoogleImageCrawler(storage={'root_dir': './coke'})
google_crawler.crawl(keyword='coke can', max_num=100)
