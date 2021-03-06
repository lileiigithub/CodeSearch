# -*- coding: utf-8 -*-
import argparse
from search import Search

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="search key word in .py files")
    parser.add_argument("-dir",help="directory,input file directory of search.")
    parser.add_argument("-words",help="words,input search words split with ‘,’.")
    args = parser.parse_args()
    ser = Search(args.dir.replace('\\','/'),args.words)
    ser.printResult()
