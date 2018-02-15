#!/usr/bin/python3
# -*- coding: utf-8 -*-

__doc__ = \
"""根据难度选择，自动导入数独网站https://www.oubk.com/蓝天九级动态数独，并予以解决。"""

import re
import time

import requests
from bs4 import BeautifulSoup

import solver


def get_url(dify):
    """输入选择难度，输出对应链接"""
    difficulty = ['super-easy',
                  'very-easy',
                  'easy',
                  'medium',
                  'hard',
                  'very-hard',
                  'insane',
                  'very-insane',
                  'super-insane']
    url_base = 'https://www.oubk.com/super-sudoku/'
    if dify in difficulty:
        return url_base + dify
    else:
        return 'wrong input'

def trytogetquestion():
    while True:
        print("Please decide the level of difficulty by entering:")
        print('super-easy/very-easy/easy/medium/hard/very-hard/insane/very-insane/super-insane\n')
        dify = input("Please enter:")
        url = get_url(dify)
        if url =='wrong input':
            print("\nWRONG: Wrong entering!!")
            print("=" * 50)
            continue
        else:
            return url

def get_question(url):
    """通过给定链接获得数独问题，并转化为队列"""
    sudoku_question = []
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'lxml')
    for i in soup.find_all('input', id=re.compile(r'k\ds\d')):
        v = i.get('value')
        if v == '':
            v = 0
        else:
            v = int(v)
        sudoku_question.append(v)
    return sudoku_question

def record_question():
    """输入数独问题的数列，格式输出到文件"""

def timer(func):
    """记录用时的装饰器"""
    def wrapper(*arg, **karg):
        t1 = time.time()
        res = func(*arg, **karg)
        t2 = time.time()
        delta_t = t2 - t1
        print('Time used:%fs' % delta_t)
        return res
    return wrapper

@timer
def solve(question):
    return solver.sudokusolve(question)

def try_again():
    trl = ['yes', 'y', 'no', 'n']
    while True:
        print('Try again?')
        print('(y)es -- try again.\n(n)o -- quit.')
        tryagain = input("Please enter:")
        if tryagain in trl:
            return tryagain
        else:
            print("\nWRONG: Wrong entering!!")
            print("=" * 50)
            continue

def main():
    while True:
        url = trytogetquestion() # 交互式的选择难度
        Q = get_question(url) # 获得问题
        solve(Q) # 解决问题
        print("=" * 50)
        tr = try_again()
        if tr in ['yes', 'y']:
            print("=" * 50)
            continue
        elif tr in ['no', 'n']:
            break

if __name__ == '__main__':
    main()
