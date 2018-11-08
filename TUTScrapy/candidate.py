# -*- coding: utf-8 -*-

import scrapy

class CandidateItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()  #Tieu de ho so
    category = scrapy.Field()  # fulltime-partime
    experience = scrapy.Field() # kinh nghiem

    career = scrapy.Field()   #Nganh nghe
    company = scrapy.Field()

    language = scrapy.Field()
    objective = scrapy.Field()
    address = scrapy.Field()
    salary=scrapy.Field()
    sex = scrapy.Field()
    age = scrapy.Field()
    position = scrapy.Field()       # Chuc vu
    contact = scrapy.Field() #Nop ho so
    expired = scrapy.Field()
    created = scrapy.Field()
    diploma = scrapy.Field() # Bang cap
    time_trial = scrapy.Field()
    url=scrapy.Field()
    pass
