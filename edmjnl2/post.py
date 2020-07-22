# -*- coding: utf-8 -*-
import scrapy

class PostSpider(scrapy.Spider):
    name = 'post_crawl'
    start_urls = ['https://financialpost.com']

    def parse(self, response):
        quotes = response.xpath('//*[@class="article-card__headline-clamp"]')
        
        for quote in quotes:
            yield {
                  'title': quote.xpath('.//text()').get(),
                  'date': "",
                  'text':"",
            }


