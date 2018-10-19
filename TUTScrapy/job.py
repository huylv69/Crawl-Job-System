# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JobItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()  #Tieu de
    category = scrapy.Field()  # fulltime-partime
    experience = scrapy.Field()

    career = scrapy.Field()   #Nganh nghe
    company = scrapy.Field()

    benefits = scrapy.Field()
    contact = scrapy.Field()
    address = scrapy.Field()
    salary=scrapy.Field()
    description = scrapy.Field()   #mo ta
    require_skill = scrapy.Field()  #yeu cau khac
    sex = scrapy.Field()
    age = scrapy.Field()
    position = scrapy.Field()       # Chuc vu
    amount = scrapy.Field()  #So luong
    contact = scrapy.Field() #Nop ho so
    expired = scrapy.Field()
    created = scrapy.Field()
    diploma = scrapy.Field() # Bang cap

    url=scrapy.Field()
    pass
