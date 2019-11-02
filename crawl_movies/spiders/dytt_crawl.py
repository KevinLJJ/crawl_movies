# -*- coding: utf-8 -*-
import scrapy


class DyttCrawlSpider(scrapy.Spider):
    name = 'dytt_crawl'
    allowed_domains = ['dytt8.net']
    start_urls = ['http://dytt8.net/']

    def parse(self, response):
        pass
