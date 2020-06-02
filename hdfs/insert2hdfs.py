#!/usr/bin/env python3
from tqdm import tqdm
from hdfs import *
import os

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

class file_file(object):
    """docstring for file_file"""
    def __init__(self, work_dir):
        self.work_dir=work_dir
        self.all_files = []
    def get_all_files(self):
        for parent, dirnames, filenames in os.walk(self.work_dir):
            for filename in filenames:
                file_path = os.path.join(parent, filename)
                self.all_files.append(file_path)
        return self.all_files

if __name__ == '__main__':
    a = pyhdfs('127.0.0.1','9870')
    a.mkdir('/ddbs')
    files = file_file('articles')
    all_files = files.get_all_files()
    for file in tqdm(all_files):
        a.upload('/ddbs',file)
