# -*- coding: utf-8 -*-
import scrapy
from fake_useragent import UserAgent

class FproxySpider(scrapy.Spider):
    name = 'fproxy'
    allowed_domains = ['free-proxy-list.net']
    ua = UserAgent()
    def start_requests(self):
        yield scrapy.Request(url='https://free-proxy-list.net',callback=self.parse,
        headers={
            'User-Agent':self.ua.random
        })

    def parse(self, response):
        row = response.xpath('//table[@class="table table-striped table-bordered"]/tbody/tr')
        for each_row in row:
            yield {
                "IP ADDRESS": each_row.xpath('.//td[1]/text()').get(),
                "PORT": each_row.xpath('.//td[2]/text()').get(),
                "HTTPS":each_row.xpath('.//td[7]/text()').get()
            }
