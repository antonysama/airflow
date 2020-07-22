# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class News4CrawlSpider(CrawlSpider):
    name = 'news_edmjnl_crawl'
    allowed_domains = ['edmontonjournal.com']
    start_urls = ['https://edmontonjournal.com']

    rules = (
        Rule(LinkExtractor(
            restrict_xpaths='//*[@class="article-card__details"]'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        yield{
            'title': response.xpath('//*[@class="article-title"]/text()').get(),
            'date': response.xpath('//*[@class="published-date__since"]/text()').get(),
            'text': response.xpath('//*[@class="article-content"]//p[normalize-space(text())]/text()').getall(), 
        }
