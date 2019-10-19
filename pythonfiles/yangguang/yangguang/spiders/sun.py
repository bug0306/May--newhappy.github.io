# -*- coding: utf-8 -*-
import scrapy

import yangguang.items

from yangguang.items import YangguangItem


class SunSpider(scrapy.Spider):
    name='sun'
    allowed_domains=['sun0769.com']
    start_urls=['http://wz.sun0769.com/index.php/question/questionType?type=4']
    def parse(self,response):
        tr_list=response.xpath("//div[@class='pagecenter']/div/table[2]/tr/td/table/tr")
        for tr in tr_list:
            item=YangguangItem()
            item['href']=tr.xpath("./td[2]/a[@class='news14']/@href").extract_first()
            item['title']=tr.xpath("./td[2]/a[@class='news14']/@title").extract_first()
            item["update_time"]=tr.xpath("./td[5]/text()").extract_first()

            yield scrapy.Request(
                item['href'],
                callback=self.parse_detail,
                meta={'item':item}
            )

        next_url=response.xpath("//a[text()='>']/@href").extract_first()
        if next_url is not None:
            yield scrapy.Request(
                next_url,
                callback=self.parse
            )

    def parse_detail(self,responce):
        item=responce.meta['item']
        item['content_img']=responce.xpath("//div[@class='wzy1']/table[2]/tr[1]/td/div["
                                           "1]/img/@src").extract()
        item['content_img']=["http://wz.sun0769.com"+i for i in item['content_img']]
        item["content"]=responce.xpath("//div[@class='wzy1']/table[2]/tr[1]/td//text()").extract()
        yield item
