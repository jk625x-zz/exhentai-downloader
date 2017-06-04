#!/usr/bin/python
#-*-coding:utf-8-*-

import random
from scrapy.downloadermiddlewares.useragent import UserAgentMiddleware
import scrapy
from scrapy.exceptions import DropItem
from scrapy.pipelines.files import FilesPipeline



class EXImagePipeline(FilesPipeline):
    def get_media_requests(self, item, info):
        yield scrapy.Request(item['image_urls'],
                                 meta={
                                     'title': item["title"]})

    def item_completed(self, results, item, info):
        file_paths = [x['path'] for ok, x in results if ok]
        if not file_paths:
            raise DropItem("Item contains no Files")
        item["file_paths"] = file_paths
        return item

    def file_path(self, request, response=None, info=None):
        title = request.meta['title']
        file_guid = title + '/' + request.url.split('/')[-1]
        filename = u'{0}'.format(file_guid)
        return filename