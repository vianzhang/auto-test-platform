#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    :author: WENHAO ZHANG
"""

import os
import sys

basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

# SQLite URI compatible windows
WIN = sys.platform.startswith('win')
if WIN:
    prefix = 'sqlite:///'
else:
    prefix = 'sqlite:////'


class BaseConfig:
    # mysql数据库配置
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@10.96.11.13:3307/auto_test?charset=utf8mb4'
    # 设置自动提交
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    # 动态追踪修改设置，如未设置只会提示警告
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # 查询时会显示原始SQL语句
    SQLALCHEMY_ECHO = True


class DevelopmentConfig(BaseConfig):
    # csrf key
    SECRET_KEY = '123456'

    IGNORE_CHECK_LOGIN_URLS = ['/static', '/login', '/register']


class TestConfig(BaseConfig):
    pass


class ProductionConfig(BaseConfig):
    pass


config = {
    'development': DevelopmentConfig,
    'test': TestConfig,
    'production': ProductionConfig
}