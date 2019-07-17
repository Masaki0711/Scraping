# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
#from myproject.items import Headline ##import MyprojectItem(item.pyで定義したクラス)に変更　
from myproject.items import MyprojectItem

class NewsCrawlSpider(CrawlSpider):
    name = '***' #spiderName
    allowed_domains = ['***.jp'] #ドメイン名
    start_urls = [
        'http://www.***/'#対象URL
        ]

    rules = (
        Rule(LinkExtractor(), callback='parse'),#ルール設定
    )

    def parse(self, response):
        item = MyprojectItem() #MyprojectItem()を変数へ格納
        for pdf in response.css('div.body'):
            #item['link'] = pdf.css('table span::text').extract()
            item['url'] = pdf.css('table a::attr(href)').extract() #PATH
        yield item
