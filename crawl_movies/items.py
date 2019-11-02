# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CrawlMoviesItem(scrapy.Item):
    movie_id = scrapy.Field()
    name = scrapy.Field()  # 影片名
    origin_name = scrapy.Field()  # 电影原名
    trans_name = scrapy.Field()  # 电影译名
    years = scrapy.Field()  # 电影年代
    length = scrapy.Field()  # 片场
    country = scrapy.Field()  # 产地
    language = scrapy.Field()  # 语言
    subtitle = scrapy.Field()  # 字幕类型
    pub_date = scrapy.Field()  # 上映日期
    source_date = scrapy.Field()  # 发布日期
    score = scrapy.Field()  # 豆瓣评分
    resolution = scrapy.Field()  # 分辨率
    director = scrapy.Field()  # 导演
    screenwriter = scrapy.Field()  # 编剧
    main_actor = scrapy.Field()  # 主演
    tag = scrapy.Field()  # 标签
    classification = scrapy.Field()  # 分类
    description = scrapy.Field()  # 简介
    cover_img = scrapy.Field()  # 封面图
    ftp_url = scrapy.Field()  # FTP地址
    magnet = scrapy.Field()  # 磁力链
