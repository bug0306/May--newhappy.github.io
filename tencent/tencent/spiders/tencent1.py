# -*- coding: utf-8 -*-
import scrapy


class Tencent1Spider(scrapy.Spider):
    name = 'tencent1'
    allowed_domains = ['careers.tencent.com']
    start_urls = ['https://careers.tencent.com/search.html/']

    def parse(self, response):
        li_list=response.xpath("//div[@class='recruit-list']/a[1]")
        for li in li_list:
            item={}
            item['tltle']=li.xpath("./h4/text()").extract_first()
            item['position']=li.xpath("./p[1]/span/text()").extract_first()
            item["content"]=li.xpath("./p[2]/text()").extract_first()
            yield item

