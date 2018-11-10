# -*- coding: utf-8 -*-

# 拉私家课列表，然后下载音频。
# 第一期可以做非登录情况下，拉部分数据。
import os
import subprocess

from pandas import json

import scrapy

api = 'https://api.zhihu.com/remix/albums'

detail = 'https://api.zhihu.com/remix/albums/1043501963178135552/detail'

playlist = 'https://api.zhihu.com/remix/albums/%s'

mixtapeIds = []

file_extension = '.mp3'
file_dir_path = os.path


class MixtapeSpider(scrapy.Spider):
    name = 'mixtape'
    allowed_domains = ['api.zhihu.com', 'baidu.com']
    start_urls = [api, 'https://www.baidu.com']

    limit = '10'
    offset = 0

    queryParma = {
        'limit': limit,
        'offset': str(offset)
    }

    def start_requests(self):
        yield scrapy.FormRequest(
            url=self.start_urls[0],
            formdata=self.queryParma,
            method='GET',
            callback=self.getMixtapeList)

    def getMixtapeList(self, response):
        mixtapelist = json.loads(response.body)
        isEnd = mixtapelist.get('paging').get('is_end')  # 测试阶段只抓第一页
        next_page = mixtapelist.get('paging').get('next')
        self.offset = next_page.split('=')[-1]
        datalist = mixtapelist['data']

        for data in datalist:
            mixtapeIds.append(data.get('id'))
            print "id = %s " % data.get('id')

        if not isEnd:
            self.offset = mixtapeIds.__len__()
            yield scrapy.FormRequest(
                url=self.start_urls[0],
                formdata={
                    'limit': self.limit,
                    'offset': str(self.offset)
                },
                method='GET',
                callback=self.getMixtapeList)
        else:
            print '获取 私家课 列表 id 集合 结束，共有 %d 条' % mixtapeIds.__len__()
            for id in mixtapeIds:
                yield scrapy.FormRequest(
                    url=playlist % id,
                    method='GET',
                    callback=self.parseMixtapeJson)

    def parseMixtapeJson(self, response):
        data = json.loads(response.body)
        file_dir = data['title']
        tracks = data['tracks']

        print '总章节 %s ' % len(tracks)

        for index, track in enumerate(tracks):
            file_name = '%s%s' % (index, track['title'])
            audio_url = track['audio']['url']
            print 'file name %s , audio url %s: ' % (file_name, audio_url)
            self.downloadAudio(file_dir, file_name, audio_url)

        pass

    def downloadAudio(self, file_dir, file_name, audio_url):
        if not os.path.exists(file_dir):
            os.mkdir(file_dir)
        youget_download_cmd = "you-get -o {} -O {}  {}".format(file_dir_path.join(file_dir),
                                                               file_name + file_extension,
                                                               audio_url)
        subprocess.call(youget_download_cmd, shell=True)


if __name__ == '__main__':
    from scrapy.cmdline import execute

    execute('scrapy crawl mixtape'.split())  # ['scrapy crawl','mixtape']

    # 'scrapy crawl amazon_products -o items.csv -t csv'.split()

    # MixtapeSpider().getMixtape()
