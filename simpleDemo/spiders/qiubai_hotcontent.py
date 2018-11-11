#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sqlite3
import sys

import scrapy
from scrapy import Request

reload(sys)
sys.setdefaultencoding('utf-8')

dbname = 'qiubai_hotcontent.db'


class ExampleSpider(scrapy.Spider):
    name = 'qiubai_hotcontent'
    allowed_domains = ['qiushibaike.com']

    start_urls = ['https://www.qiushibaike.com/8hr/page/1/']

    content = []
    author = []

    write_db_enbale = False

    def __init__(self):
        self.conn = sqlite3.connect(dbname)
        self.dropTable()
        self.createTable()

    def parse(self, response):
        user_info = response.xpath('//div[@class="author clearfix"]')

        for li in user_info:
            item = li.xpath('.//h2/text()').extract()[0]
            self.author.append(item)
        print '作者人数：{}'.format(str(len(self.author)))

        content_inf = response.xpath('//div[@class="content"]')
        for content in content_inf:
            lineContent = ""
            contentList = content.xpath('span/text()').extract()
            for line in contentList:
                lineContent += line

            self.content.append(lineContent)
            print("%s " % lineContent)

        print '内容条数：{}'.format(len(self.content))

        # 提取下一页链接
        hrefs = response.xpath('//a/@href').extract()
        for index in range(0, len(hrefs)):
            short_url = hrefs[index]
            # print short_url
            curr_page = str(response.url).split('/')[-2]
            next_page_num = int(curr_page) + 1
            next_page = '/8hr/page/{}/'.format(next_page_num)
            if short_url == next_page:
                next_url = 'https://www.qiushibaike.com' + short_url
                self.write_db_enbale = False
                yield Request(next_url, callback=self.parse)  # 递归的去访问URL　
                break
            else:
                self.write_db_enbale = True
        if not self.write_db_enbale:
            return

        # 最后写入
        try:
            cursor = self.conn.cursor()
            for index in range(0, self.author.__sizeof__(), 1):
                # print 'insert index = {}'.format(index)
                self.insertTable(self.author[index], self.content[index], cursor)

        except  Exception as e:
            self.log('exceptin' + e.message)

        finally:
            self.log('-----------end---------')

            cursor.close()

    pass

    def dropTable(self):
        sql_drop = '''
         drop table if exists hotcontent;
        '''

        cursor = self.conn.cursor()
        cursor.execute(sql_drop)
        cursor.close()

    def createTable(self):
        sql_create = '''

                 create table hotcontent(
                        [id]  integer PRIMARY KEY autoincrement,
                        [author] int default 0,
                        [content] blob,
                        [createdate]  datetime default (datetime('now', 'localtime'))
                        );
                     '''
        # sql_create = 'drop table hotcontent;' varchar (150)
        cursor = self.conn.cursor()
        cursor.execute(sql_create)
        cursor.close()

    def insertTable(self, author, content, cursor):
        sql_insert = '''
                insert into hotcontent([author],[content])
                        values(:author,:content)

                    '''

        cursor.execute(sql_insert, {'author': author,
                                    'content': content})
        self.conn.commit()


if __name__ == '__main__':
    from scrapy.cmdline import execute

    execute('scrapy crawl qiubai_hotcontent'.split())
