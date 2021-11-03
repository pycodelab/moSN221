# -*- coding: utf-8 -*-
"""
Created on Tue May  4 12:56:33 2021

@author: diawm
"""

import scrapy

class BlogSpider(scrapy.Spider):
    name = "characterspider"
    start_urls = ['https://fr.wikipedia.org/wiki/Cat%C3%A9gorie:Personnage_d\'animation']
    
    def parse(self,response):
        for link in response.css('div#mw-pages div.mw-content-ltr li'):
            yield{'character':link.css('a::text').extract_first()}