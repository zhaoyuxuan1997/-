#!/usr/bin/env python3
from tqdm import tqdm
from hdfs import *
import os
from flask import Flask, request, redirect, url_for, render_template, flash,send_file, send_from_directory,make_response


class pyhdfs(object):
    """docstring for pyhdfs"""
    def __init__(self, ip,port):
        self.ip = ip
        self.port = port
        self.url = 'http://'+self.ip+':'+self.port
        self.client = Client(self.url)
    def mkdir(self,dirname,permission=''):
        if permission:
            permission = int(permission)
        else:
            permission = 644
        self.client.makedirs(dirname,permission = permission)
    def rmdir(self,dirname):
        self.client.delete(dirname,True)
    def upload(self,dirname,filename):
        self.client.upload(dirname,filename)
    def download(self,filename,download_filename):
        self.client.download(filename,download_filename)
    def cat(self,filename):
        with self.client.read(filename) as f:
            return f.read()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route("/download/<filename>", methods=['GET'])
def download_file(filename):
    # 需要知道2个参数, 第1个参数是本地目录的path, 第2个参数是文件名(带扩展名)
    directory = '/home/zyx/ddbs/files/'
    a = pyhdfs('127.0.0.1','9870')
    filename1='/ddbs/'+filename
    try:
        a.download(filename1,directory)
    except:
        pass
    return send_from_directory(directory, filename, as_attachment=True)

@app.route("/download1/<filename>", methods=['GET'])
def download_file1(filename):
    # 需要知道2个参数, 第1个参数是本地目录的path, 第2个参数是文件名(带扩展名)
    directory = '/home/zyx/ddbs/files/'
    a = pyhdfs('127.0.0.1','9870')
    filename1='/ddbs/'+filename
    try:
        a.download(filename1,directory)
    except:
        pass
    response = make_response(send_from_directory(directory, filename, as_attachment=True))
    response.headers["Content-Disposition"] = "attachment; filename={}".format(file_name.encode().decode('latin-1'))
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9871, debug=False)
