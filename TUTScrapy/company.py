# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CompanyItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    scale = scrapy.Field()
    about = scrapy.Field()
    address = scrapy.Field()
    website = scrapy.Field()
    url = scrapy.Field()
    pass
