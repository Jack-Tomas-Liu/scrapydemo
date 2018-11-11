# -*- coding: utf-8 -*-
import sys

from scrapy.linkextractors import LinkExtractor
from scrapy.spiders.crawl import CrawlSpider, Rule

reload(sys)
sys.setdefaultencoding('utf-8')


class QiubaiSpider(CrawlSpider):
    name = 'qiubai'
    allowed_domains = ['qiushibaike.com']
    start_urls = ['https://www.qiushibaike.com/8hr/page/1/']

    rules = [
        # allow:提取符合对应正则表达式的链接，deny相反
        # restrict_xpaths使用xpath和正则表达式共同作用
        # allow_domains,deny_domains
        # follow是否沿着链接往下追踪
        Rule(LinkExtractor(allow='.*?/8hr/page/\d'), callback='parse_item', follow=True),
    ]

    def parse_item(self, response):
        user_info = response.xpath('//div[@class="author clearfix"]')
        content_info = response.xpath('//div[@class="content"]')

        for li, content in zip(user_info, content_info):

            from simpleDemo.items import QiubaiItem
            item = QiubaiItem()

            item['author'] = li.xpath('.//h2/text()').extract()[0]

            lineContent = ""
            contentList = content.xpath('span/text()').extract()
            for line in contentList:
                lineContent += line

            item['content'] = lineContent

            yield item



if __name__ == '__main__':
    from scrapy.cmdline import execute

    execute('scrapy crawl qiubai'.split())
