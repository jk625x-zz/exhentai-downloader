# -*- coding: utf-8 -*-

BOT_NAME = 'exhentai'

SPIDER_MODULES = ['exhentai.spiders']
NEWSPIDER_MODULE = 'exhentai.spiders'


ROBOTSTXT_OBEY = True
CONCURRENT_REQUESTS = 16 # it seems OK
DOWNLOAD_DELAY = 3
RANDOMIZE_DOWNLOAD_DELAY = True
CONCURRENT_REQUESTS_PER_DOMAIN = 16
CONCURRENT_REQUESTS_PER_IP = 16

ITEM_PIPELINES = {
   'exhentai.pipelines.EXImagePipeline': 1
}
DOWNLOADER_MIDDLEWARES = {
        'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware' : None,
        'exhentai.middlewares.RotateUserAgentMiddleware' :400
}

FILES_STORE = "/Users/jk_625/pic"

DOWNLOAD_TIMEOUT = 5 * 60
AUTOTHROTTLE_START_DELAY = 5
AUTOTHROTTLE_MAX_DELAY = 60
AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0

# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

