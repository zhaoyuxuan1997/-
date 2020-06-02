#!/usr/bin/python3
#coding:utf8
from flask import Flask, request, redirect, url_for, render_template, flash,send_file, send_from_directory,make_response,jsonify,Response
import pymongo
from flask_cors import CORS
app = Flask(__name__)
CORS(app, resources=r'/*')
class mongopy(object):
    """docstring for mongopy"""
    def __init__(self, db,col):
        self.client = pymongo.MongoClient("mongodb://172.22.0.8:27017/")
        self.db = self.client[db]
        self.col = self.db[col]

    def search_popular(self,time='',temporalGranularity=''):
        # print({"_id":{'$regex' : ".*{}.*".format(time)},"temporalGranularity":temporalGranularity})
        for x in self.col.find({"_id":{'$regex' : ".*{}.*".format(time)},"temporalGranularity":temporalGranularity},{"articleAidList":1}):
            return x
    def search_aid(self,aid):
        for x in self.col.find({"aid":aid},{"text":1,"image":1,"video":1,"title":1}):
            return x
    def search_uid(self,uid):
        result = []
        for x in self.col.find({"uid":uid},{"aid":1}):
            result.append(x)
        return result


@app.route('/')
def index():
    return render_template('mongo_flask.html')


@app.route('/search_popular')
def flask_search():
    time = request.args.get('time')
    temporalGranularity = request.args.get('temporalGranularity')
    a = mongopy('ddbs','popular_rank')
    popular_result = a.search_popular(time,temporalGranularity)
    # {'_id': '2017-12-01T00:00:00.000Zmonthly', 'articleAidList': ['4909', '4184', '8392', '5442', '8652']}
    articleAidList = popular_result['articleAidList']
    b = mongopy('ddbs','article')
    articleAidList_all = []
    for aid in articleAidList:
        aid_result = b.search_aid(aid)
        tmp_texts = aid_result['text'].split(',')
        tmp_images = aid_result['image'].split(',')
        tmp_videos = aid_result['video'].split(',')
        for i in range(len(tmp_texts)):
            if tmp_texts[i]:
                tmp_texts[i] += ' link:http://202.112.51.43:9871/download/'+tmp_texts[i]
        for i in range(len(tmp_images)):
            if tmp_images[i]:
                tmp_images[i] += ' link:http://202.112.51.43:9871/download/'+tmp_images[i]
        for i in range(len(tmp_videos)):
            if tmp_videos[i]:
                tmp_videos[i] += ' link:http://202.112.51.43:9871/download/'+tmp_videos[i]
        article_result = {'texts':tmp_texts,'images':tmp_images,'videos':tmp_videos,'title':aid_result['title']}
        articleAidList_all.append(article_result)
        # print(article_result)
        aid_result['text'] = aid_result['text']+' link'
    ret = {"popular_result": popular_result,"articleAidList_all":articleAidList_all}
    return jsonify(ret)
    # return Response("callback("+str(ret)+")")

@app.route('/search_user_read')
def search_user_read():
    uid = request.args.get('uid')
    a = mongopy('ddbs','read')
    result=a.search_uid(uid)
    aids = []
    for aid in result:
        aids.append(aid['aid'])
    b = mongopy('ddbs','article')
    articleAidList_all = []
    for aid in aids:
        aid_result = b.search_aid(aid)
        tmp_texts = aid_result['text'].split(',')
        tmp_images = aid_result['image'].split(',')
        tmp_videos = aid_result['video'].split(',')
        for i in range(len(tmp_texts)):
            if tmp_texts[i]:
                tmp_texts[i] += ' link:http://202.112.51.43:9871/download/'+tmp_texts[i]
        for i in range(len(tmp_images)):
            if tmp_images[i]:
                tmp_images[i] += ' link:http://202.112.51.43:9871/download/'+tmp_images[i]
        for i in range(len(tmp_videos)):
            if tmp_videos[i]:
                tmp_videos[i] += ' link:http://202.112.51.43:9871/download/'+tmp_videos[i]
        article_result = {'texts':tmp_texts,'images':tmp_images,'videos':tmp_videos,'title':aid_result['title']}
        articleAidList_all.append(article_result)
        # print(article_result)
        aid_result['text'] = aid_result['text']+' link'
    # print(aid)
    ret = {"uid_read_aid":aids,"articleAidList_all":articleAidList_all}
    return jsonify(ret)
    # return Response("callback("+str(ret)+")")



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9872, debug=False)
