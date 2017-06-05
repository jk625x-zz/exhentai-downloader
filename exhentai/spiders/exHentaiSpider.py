# -*- coding: utf-8 -*-
import logging
import scrapy
from scrapy import FormRequest

from exhentai.items import ImageItem


class ExHentaiSpider(scrapy.Spider):
    TAG = 'ExHentaiSpider'
    name = 'exhentai'

    def __init__(self,user,rule):
        self.username = user['username']
        self.password = user['password']
        self.rule = rule
        self.page = 1

    def start_requests(self):
        print 'Login Step 1'
        return [scrapy.FormRequest("https://forums.e-hentai.org/index.php?act=Login&CODE=01&CookieDate=1",
                              meta={'cookiejar': 1},
                              formdata={'UserName': self.username,
                                       'PassWord': self.password},
                              callback=self.first_login,
                              dont_filter=True)]

    def first_login(self, response):
        print 'Login Step 2'
        return [scrapy.Request("https://exhentai.org/",
                              meta={'cookiejar': response.meta['cookiejar']},
                              callback=self.second_login,
                              dont_filter=True)]

    # need the step 2 to fetch complete cookies 
    def second_login(self, response):
        print 'Scraw Start'
        return[scrapy.Request(
            "https://exhentai.org/?f_doujinshi={0}&f_manga={1}&f_artistcg={2}&f_gamecg={3}&f_western={4}&f_non-h={5}&f_imageset={6}&f_cosplay={7}&f_asianporn={8}&f_misc={9}&f_search={10}&f_apply=Apply+Filter&inline_set=dm_t"
            .format(self.rule['doujinshi'],
                    self.rule['manga'],
                    self.rule['artist_cg'],
                    self.rule['game_cg'],
                    self.rule['western'],
                    self.rule['non_h'],
                    self.rule['image_set'],
                    self.rule['cosplay'],
                    self.rule['asian_porn'],
                    self.rule['misc'],
                    self.rule['keyword'],),
            meta={'cookiejar': response.meta['cookiejar']})]


    def parse(self, response):
        articles = response.css('.id2 a::attr(href)').extract()
        next = response.xpath('//table[@class="ptt"]/tr/td[last()]/a/@href').extract_first()

        for article in articles:
            if self.page >= self.rule['start_page'] and self.page <= self.rule['end_page']:
                yield scrapy.Request(article,
                                 callback=self.parse_article,
                                 meta={'cookiejar': response.meta['cookiejar']})
            if self.page > self.rule['end_page']:
                break
            print 'Loading Page:' + self.page
            self.page += 1


        if next != None:
            yield scrapy.Request(next,
                                 callback=self.parse,
                                 meta={'cookiejar': response.meta['cookiejar']})


    def parse_article(self, response):
        pics = response.css('.gdtm a::attr(href)').extract()
        title = response.xpath('//h1[@id="gn"]/text()').extract_first()
        next = response.xpath('//div[@class="gtb"]/table/tr/td[last()]/a/@href').extract_first()
        fav = int((response.xpath('//td[@id="favcount"]/text()').re(r'[0-9]+') or ['1'])[0])
        star = float(response.xpath('//td[@id="rating_label"]/text()').re(r'[0-9]+\.[0-9]+')[0])
        if fav < self.rule['fav'] or star < self.rule['star']:
            print '-Dropped-' + 'title:' + title
            print 'favourite: ' + fav + ' , ' + 'stars: ' + star
            return

        print '-Dowloading-' + 'title:' + title
        print 'favourite: ' + fav + ' , ' + 'stars: ' + star 

        if next != None:
            yield scrapy.Request(next,
                                callback=self.parse_article,
                                meta={'cookiejar': response.meta['cookiejar'],
                                       'title': title})
        for pic in pics:
            yield scrapy.Request(pic,
                                 callback=self.parse_img,
                                 meta={'cookiejar': response.meta['cookiejar'],
                                       'title': title})


    def parse_img(self, response):
        img_url = response.xpath('//div[@id="i3"]/a/img/@src').extract_first()
        item = ImageItem()
        item["title"] = response.meta['title']
        item["image_urls"] = img_url
        yield item






