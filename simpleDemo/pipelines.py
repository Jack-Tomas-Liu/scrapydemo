# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sqlite3

dbname = 'qiubai.db'

sql_drop = '''
         drop table if exists hotcontent;
        '''

sql_create = '''

                create table hotcontent(
                       [id]  integer PRIMARY KEY autoincrement,
                       [author] int default 0,
                       [content] blob,
                       [createdate]  datetime default (datetime('now', 'localtime'))
                       );
                    '''

sql_insert = '''
                  insert into hotcontent([author],[content])
                          values(:author,:content)

                      '''

conn = sqlite3.connect(dbname)
cursor = conn.cursor()

class SimpledemoPipeline(object):

    def __init__(self):
        self.dropTable()
        self.createTable()
        pass

    def dropTable(self):
        cursor.execute(sql_drop)
        # conn.commit()

    def createTable(self):
        # sql_create = 'drop table hotcontent;' varchar (150)
        cursor.execute(sql_create)
        # conn.commit()

    def insertTable(self, author, content):
        cursor.execute(sql_insert, {'author': author,
                                    'content': content})
        conn.commit()

    def process_item(self, item, spider):
        self.insertTable(item['author'], item['content'])
        return item

    def open_spider(self, spider):
        pass

    def close_spider(self, spider):
        cursor.close()
        pass
