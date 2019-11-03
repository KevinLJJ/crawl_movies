# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from crawl_movies.models.mongo import MovieDetail, WorkerDetail


class CrawlMoviesPipeline(object):
    def process_item(self, item, spider):
        """
        管道接受item
        :param item:
        :param spider:
        :return:
        """
        # 当前数据是否存在
        saved = MovieDetail.objects(movie_id=item['movie_id'])
        # 不存在则添加
        if not saved:
            self.save_movie_data(item)
        return item

    def save_movie_data(self, item):
        """
        保存电影详情
        :param item:
        :return:
        """
        movie = MovieDetail()
        movie.movie_id = item.get('movie_id', '')
        movie.magnet = self.splite_magnet(item.get('magnet', ''))
        pass

    def split_words(self, words: str, flag):
        """
        人名分词
        :param words:
        :param flag:
        :return:
        """
        if flag == 'name':
            words = words.replace('　', '')
            if words.find('<br>') != -1:
                words.split(' <br> ')
            return words

    def splite_magnet(self, url):
        """
        清洗磁力链
        :param url:
        :return:
        """
        return url.replace('amp;', '') if url else ''

