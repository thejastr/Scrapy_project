# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AptiquesItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #question = scrapy.Field()
    option1= scrapy.Field()
    option2= scrapy.Field()
    option3= scrapy.Field()
    option4= scrapy.Field()
    option5= scrapy.Field() 
    _question = scrapy.Field()

