import numpy as np
import json
import paddle
import paddle as P
import paddle.nn as nn
import paddle.nn.functional as F
from datetime import datetime
from flask import render_template, request,Flask
from run import app
from wxcloudrun.dao import delete_counterbyid, query_counterbyid, insert_counter, update_counterbyid
from wxcloudrun.model import Counters
from wxcloudrun.response import make_succ_empty_response, make_succ_response, make_err_response
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import  os
import jieba

@app.route('/upload', methods=['POST'])
def upload():
    all_files = [f for f in os.listdir('/app')]
    return str(all_files) #获取当前工作目录路径
    global changtoushis
    text = request.form.get('text')
    print(text)
    acrostic = json.loads(text)
    print(acrostic)
    changtoushis = show2(acrostic=acrostic, prefix='一二三四五六七，七六五四三二一。', net = net)
    print(changtoushis)
    return changtoushis

@app.route('/upload1', methods=['POST'])
def upload1():
    global xuxieshi1
    text = request.form.get('text')
    print(text)
    acrostic = json.loads(text)
    print(acrostic)
    xuxieshi1 = show1(result=acrostic, prefix='明日何其多，总管一二三。', net = net)
    print(xuxieshi1)
    return xuxieshi1

