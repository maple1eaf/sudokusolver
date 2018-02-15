#!/usr/bin/python3
# -*- coding:utf-8 -*- 

"""自定义数独求解"""

"""
说明：
待求解的自定义数独请按下列格式覆盖程序中的question列表（其中未知的数以数字0填充）：
question = [
0, 0, 0, 0, 0, 0, 0, 0, 0,
0, 0, 0, 0, 0, 0, 0, 0, 0,
0, 0, 0, 0, 0, 0, 0, 0, 0,
0, 0, 0, 0, 0, 0, 0, 0, 0,
0, 0, 0, 0, 0, 0, 0, 0, 0,
0, 0, 0, 0, 0, 0, 0, 0, 0,
0, 0, 0, 0, 0, 0, 0, 0, 0,
0, 0, 0, 0, 0, 0, 0, 0, 0,
0, 0, 0, 0, 0, 0, 0, 0, 0]
"""

# 自定义数独：
question = [
8, 0, 0, 0, 0, 0, 0, 0, 0,
0, 0, 3, 6, 0, 0, 0, 0, 0,
0, 7, 0, 0, 9, 0, 2, 0, 0,
0, 5, 0, 0, 0, 7, 0, 0, 0,
0, 0, 0, 0, 4, 5, 7, 0, 0,
0, 0, 0, 1, 0, 0, 0, 3, 0,
0, 0, 1, 0, 0, 0, 0, 6, 8,
0, 0, 8, 5, 0, 0, 0, 1, 0,
0, 9, 0, 0, 0, 0, 4, 0, 0]

import sudoku_solver
import time

def main():
    time_begin = time.time()# 计时开始
    existsolution, sudoku_answer = sudoku_solver.sudokusolve(question)# 解题
    time_end = time.time()# 计时结束
    print("Time used:", time_end-time_begin,"s")# 输出解题时间

if __name__ == "__main__":
    main()
