# -*- coding: utf-8 -*-
import os
from config import Config
import shutil
import sys

class Search(object):
    def __init__(self,_dir,_keyword):
        # _dir: dir
        # _keyword: list of keyword
        self.dir = _dir
        self.keyword = _keyword
        self.prasedFiles_list = []
        self.prasedWord_list = []
        self.searchResult = []  # file,line,contains
        self.matchCase = Config.matchCase  # match case
        self.searchFileType = Config.searchFileType

        self.praseFiles()
        self.praseKeywords()
        self.filterSearchFile()
        self.matchWords()

    def praseFiles(self):
        PATH = self.dir
        for root, dirs, files in os.walk(PATH):
            for name in files:
                filename = os.path.join(root, name)
                self.prasedFiles_list.append(filename)

    def praseKeywords(self):
        self.prasedWord_list = self.keyword.split(";")

    def matchWords(self):
        for filePath in self.prasedFiles_list:
            try:
                self.praseContent(filePath, "utf-8")
            except:
                try:
                    self.praseContent(filePath, "gbk")
                except Exception as err:
                    print("cannot prase file:",filePath)
                    print(err)
                continue

    def praseContent(self,_file_path,_encodec):
        filePath = _file_path
        encodc = _encodec
        with open(filePath, encoding=encodc) as file:
            contains = file.readlines()
            length =   len(contains)
            for i in range(length):
                if self.matchCase == False:  # don't match case
                    lower_line = contains[i].lower()
                for word in self.prasedWord_list:
                    if lower_line.count(word.lower()):
                        info = (filePath, i, self.matchLine(contains,i,length,Config.beforeNum,Config.afterNum))
                        self.searchResult.append(info)

    def matchLine(self,_contains,_i,_maxindex,_beforeN,_afterN):
        start = max(0,_i-_beforeN)
        end = min(_maxindex,_i+_afterN)
        lines = ""
        for index in range(start,end+1):
            if _contains[index].strip()!="":
                lines += _contains[index]
        return lines

    def printResult(self):
        results = self.searchResult
        for i in range(len(results)):
            print(str(i)+": "+ results[i][0]+": "+str(results[i][1]))
            print(results[i][2])

    def setmatchCase(self,_bool):
        # 设置匹配大小写
        self.matchCase = _bool

    def filterSearchFile(self):
        # 过滤非查找文件类型
        Files_list = []
        for filePath in self.prasedFiles_list:
            filetype = filePath.split(".")[-1]
            if filetype in self.searchFileType:
                Files_list.append(filePath)
        self.prasedFiles_list = Files_list

if __name__ == '__main__':
    DIR = r"I:\Practice\Python"
    DIR1 = r"I:\Projects\pyqt5-master"
    KEYWORDS="QLabel"
    search = Search(DIR1,KEYWORDS)
    search.printResult()
    # search.check_file()
