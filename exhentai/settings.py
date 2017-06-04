# -*- coding: utf-8 -*-

BOT_NAME = 'exhentai'

SPIDER_MODULES = ['exhentai.spiders']
NEWSPIDER_MODULE = 'exhentai.spiders'


ROBOTSTXT_OBEY = False
CONCURRENT_REQUESTS = 32
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

DOWNLOAD_MAXSIZE = 325674803
DOWNLOAD_WARNSIZE = 325674803
DOWNLOAD_TIMEOUT = 30 * 60
AUTOTHROTTLE_START_DELAY = 5
AUTOTHROTTLE_MAX_DELAY = 60
AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0

# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

