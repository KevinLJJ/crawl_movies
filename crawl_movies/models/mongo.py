# -*- coding: utf-8 -*-
# @Time    : 2019-11-03 13:04
# @Author  : ljj0452@gmail.com
import datetime

from mongoengine import (
    Document,
    StringField,
    DateTimeField,
    IntField,
    FloatField,
    BooleanField,
    EmbeddedDocument,
    EmbeddedDocumentListField
)


class WorkerDetail(EmbeddedDocument):
    """
    演职人员
    """
    ch_name = StringField(verbose="中文名", default='')
    en_name = StringField(verbose="英文名", default='')

    def to_dict(self):
        return {
            'ch_name': self.ch_name,
            'en_name': self.en_name
        }


class MovieDetail(Document):
    """
    影片详情
    """
    movie_id = StringField(verbose="标识ID", default='')
    name = StringField(verbose="电影名", default='')
    origin_name = StringField(verbose="电影原名", default='')
    trans_name = StringField(verbose="电影译名", default='')
    years = StringField(verbose="年代", default='')
    length = StringField(verbose="片长", default='')
    country = StringField(verbose="发行地区", default='')
    language = StringField(verbose="语言", default='')
    subtitle = StringField(verbose="字幕类型", default='')
    pub_date = StringField(verbose="上映日期", default='')
    source_date = StringField(verbose="资源日期", default='')
    score = StringField(verbose="评分", default='')
    resolution = StringField(verbose="分辨率", default='')
    director = EmbeddedDocumentListField(WorkerDetail, verbose="导演", default=[])
    screenwriter = EmbeddedDocumentListField(WorkerDetail, verbose="编剧", default=[])
    main_actor = EmbeddedDocumentListField(WorkerDetail, verbose="主演列表", default=[])
    tag = StringField(verbose="标签", default='')
    classification = StringField(verbose="分类", default='')
    description = StringField(verbose="简介", default='')
    cover_img = StringField(verbose="封面图", default='')
    ftp_url = StringField(verbose="FTP地址", default='')
    magnet = StringField(verbose="磁力链", default='')
    update_time = DateTimeField(verbose="更新时间", default=None)

    def to_dict(self):
        return {
            'movie_id': self.movie_id,
            'name': self.name,
            'origin_name': self.origin_name,
            'trans_name': self.trans_name,
            'years': self.years,
            'length': self.length,
            'country': self.country,
            'language': self.language,
            'subtitle': self.subtitle,
            'pub_date': self.pub_date,
            'source_date': self.source_date,
            'socre': self.score,
            'resolution': self.resolution,
            'director': self.director,
            'screenwriter': self.screenwriter,
            'main_actor': self.main_actor,
            'tag': self.tag,
            'classification': self.classification,
            'description': self.description,
            'cover_img': self.cover_img,
            'ftp_url': self.ftp_url,
            'magnet': self.magnet,
            'update': self.update_time
        }

    def save(self, *args, **kwargs):
        self.update_time = datetime.datetime.now()
        return super(MovieDetail, self).save(*args, **kwargs)
