# -*- coding: utf-8 -*-
# @Time    : 2019-11-02 16:53
# @Author  : ljj0452@gmail.com

import os

from scrapy import cmdline


def crawl_start(one_name):
    cmdline.execute(f'scrapy crawl {one_name}'.split())


if __name__ == '__main__':
    print(os.getcwd())
    name = 'dytt_crawl'
    crawl_start(name)
