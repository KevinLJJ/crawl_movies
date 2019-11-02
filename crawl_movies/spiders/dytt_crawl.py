# -*- coding: utf-8 -*-
import re
import scrapy
from crawl_movies.items import CrawlMoviesItem


class DyttCrawlSpider(scrapy.Spider):
    name = 'dytt_crawl'
    allowed_domains = ['dytt8.net']

    # 主站地址
    site = 'https://www.dytt8.net'

    # 入口地址
    start_urls = [f'{site}/html/gndy/dyzz/list_23_1.html']

    def parse(self, response):
        """
        解析列表页面
        :param response: 响应列表内容
        :return:
        """
        # 匹配列表
        movie_list = response.xpath('//a[@class="ulink"]/@href').extract()
        if movie_list:
            for movie_url in movie_list:
                yield scrapy.Request(url=f'{self.site}{movie_url}', callback=self.get_detail, dont_filter=True)

    def get_detail(self, response):
        """
        电影详情规则解析
        :param response:
        :return:
        """
        items = CrawlMoviesItem()
        items['movie_id'] = '-'.join(response.url[:-5].split('/')[-2:])
        title = re.search(r'《(.*?)》', str(response.xpath('//title/text()')))
        items['name'] = self.reg_match(title)
        content = response.xpath('//div[@class="co_content8"]').extract()[0]
        if content:
            items['origin_name'] = self.reg_match(re.search(r'◎片　　名　(.*?) <br>', content))
            items['trans_name'] = self.reg_match(re.search(r'◎译　　名　(.*?) <br>', content))
            items['years'] = self.reg_match(re.search(r'◎年　　代　(.*?) <br>', content))
            items['length'] = self.reg_match(re.search(r'◎片　　长　(.*?) <br>', content))
            items['country'] = self.reg_match(re.search(r'◎产　　地　(.*?) <br>', content))
            items['language'] = self.reg_match(re.search(r'◎语　　言　(.*?) <br>', content))
            items['subtitle'] = self.reg_match(re.search(r'◎字　　幕　(.*?) <br>', content))
            items['pub_date'] = self.reg_match(re.search(r'◎上映日期　(.*?) <br>', content))
            items['source_date'] = self.reg_match(re.search(r'◎产　　地　(.*?) <br>', content))
            items['score'] = self.reg_match(re.search(r'◎豆瓣评分　(.*?) <br>', content))
            items['resolution'] = self.reg_match(re.search(r'◎视频尺寸　(.*?) <br>', content))
            items['director'] = self.reg_match(re.search(r'◎导　　演　(.*?) <br>', content))
            items['screenwriter'] = self.reg_match(re.search(r'◎编　　剧　(.*?) <br>', content))
            items['main_actor'] = self.reg_match(re.search(r'◎主　　演　(.*?) <br>', content))
            items['tag'] = self.reg_match(re.search(r'◎标　　签　(.*?) <br>', content))
            items['classification'] = self.reg_match(re.search(r'◎类　　别　(.*?) <br>', content))
            items['description'] = self.reg_match(re.search(r'◎简　　介 <br><br>　　(.*?) <br><br>', content))
            items['cover_img'] = self.reg_match(re.search(r'src="(https://extraimage.net.*?.jpg)', content))
            items['ftp_url'] = self.reg_match(re.search(r'href="(ftp://ygdy8.*?)">', content))
            items['magnet'] = self.reg_match(re.search(r'a href="(magnet.*?fannounce)"', content))
        yield items

    def reg_match(self, result):
        """
        正则匹配
        :param result:
        :return:
        """
        return result.group(1) if result else ''
