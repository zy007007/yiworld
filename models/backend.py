# -*- coding:utf-8 -*-
from config.ext import mongo
import datetime


class DailycostDoc(mongo.DynamicDocument):
    type = mongo.StringField()
    money = mongo.FloatField()
    date = mongo.DateTimeField(default=datetime.datetime.now)