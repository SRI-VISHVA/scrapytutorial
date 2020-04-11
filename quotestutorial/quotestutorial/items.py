# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
# Extracted data -> Temporary Location(Items) -> json/csv/xml
# Extracted data -> Temporary Location(Items) -> pipelines -> Sql/Mongo DB
import scrapy


class QuotestutorialItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    author = scrapy.Field()
    tags = scrapy.Field()
