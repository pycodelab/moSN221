# -*- coding: utf-8 -*-
"""
Created on Tue May  4 12:26:13 2021

@author: diawm
"""

import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls=["https://quotes.toscrape.com/tag/humor",]
    
    def parse(self, response, kwargs):
        for quote in response.css("div.quote"):
            yield {
                "text": quote.css("span.text::text").extract_first(),
                "author": quote.xpath("span/small/text()").extract_first(),
                }
            
        next_page = response.css('li.next a::attr("href")').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)