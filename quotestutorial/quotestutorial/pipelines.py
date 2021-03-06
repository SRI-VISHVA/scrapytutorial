# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# Extracted data -> Temporary Location(Items) -> json/csv/xml
# Extracted data -> Temporary Location(Items) -> pipelines -> Sql/Mongo DB
import sqlite3


class QuotestutorialPipeline(object):

    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = sqlite3.connect('myquotes.db')
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS quotes_db""")
        self.curr.execute("""create table quotes_db(title text, author text, tags text)""")

    def process_item(self, item, spider):
        self.store_db(item)
        # print('Pipeline:' + item['title'][0])
        return item

    def store_db(self, item):
        # print(item['title'][0])
        self.curr.execute("""INSERT INTO quotes_db VALUES (?, ?, ?)""",
                          (item['title'][0], item['author'][0], item['tags'][0],))
        self.conn.commit()
