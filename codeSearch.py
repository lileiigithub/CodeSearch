# -*- coding: utf-8 -*-
import os
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
        self.matchCase = False  # match case
        self.searchFileType = ["py"]

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
        lineNumber = 0
        with open(filePath, encoding=encodc) as file:
            for line in file.readlines():
                if self.matchCase == False:  # don't match case
                    lower_line = line.lower()
                for word in self.prasedWord_list:
                    if lower_line.count(word):
                        self.searchResult.append((filePath, lineNumber, line))
                lineNumber += 1

    def printResult(self):
        for result in self.searchResult:
            print(result[0]+":")
            print(str(result[1]) + " "+result[2])

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
    KEYWORDS="except"
    search = Search(DIR,KEYWORDS)
    search.printResult()
    # search.check_file()
