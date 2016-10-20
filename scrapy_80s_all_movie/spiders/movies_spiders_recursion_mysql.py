import scrapy, re
from twisted.enterprise import adbapi
from scrapy_80s_all_movie.items import Scrapy80SAllMovieItem
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class Movies_Spider(scrapy.spiders.Spider):
    name = 'movies_recursion_mysql'
    allowed_domains = ["80s.tw"]
    start_urls = ["http://www.80s.tw/movie/list/----h"]

    def parse_after(self, response):
        item = Scrapy80SAllMovieItem()
        selector = scrapy.Selector(response)
        link =  selector.xpath('//span[@class="xunlei dlbutton1"]/a/@href').extract()[0]
        item['name'] = response.meta['name']
        item['link'] = link
        item['desc'] = response.meta['desc']
        print 'abc' + item['name'] + item['link'] + item['desc']
        print type(item['name'])
        return  item

    def parse(self, response):
        selector = scrapy.Selector(response)
        movies = selector.xpath('//div[@class="clearfix noborder block1"]/ul[@class="me1 clearfix"]/li')

        num = 0
        for i in movies:
            name = i.xpath('h3/a/text()').extract()[0]
            name = name.replace(' ', '').replace('\n', '')
            desc = i.xpath('span[@class="tip"]/text()').extract()[0]
            desc = desc.replace(' ', '').replace('\n', '')
            link = 'http://www.80s.tw' + i.xpath('a//@href').extract()[0]
            yield scrapy.http.Request(url=link, meta={'name':name,'desc':desc} ,callback=self.parse_after)

