import scrapy


class Firstspider01Spider(scrapy.Spider):
    name = 'firstspider_01'
    allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.xxx.com/']

    def parse(self, response):
        pass
