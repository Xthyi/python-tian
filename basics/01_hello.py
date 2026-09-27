# -*- coding: utf-8 -*-
"""
01 - 第一个 Python 程序：变量与输出

运行方式（在终端里）：
    python3 basics/01_hello.py
"""

# ---- 变量：不需要声明类型，直接赋值 ----
name = "Xthyi"          # 字符串 str
age = 19                # 整数 int
height = 1.75           # 浮点数 float
is_student = True       # 布尔值 bool

# ---- print：把内容打印到屏幕 ----
print("你好，Python！")
print(f"我叫 {name}，今年 {age} 岁，身高 {height} 米")
print(f"我是学生吗？{is_student}")

# ---- f-string：在字符串里嵌变量，最常用的输出方式 ----
print(f"{name} 明年就 {age + 1} 岁了")

# ---- 简单运算 ----
print("1 + 2 =", 1 + 2)
print("10 / 3 =", 10 / 3)       # 除法，结果是浮点数
print("10 // 3 =", 10 // 3)     # 整除，丢掉小数
print("10 % 3 =", 10 % 3)       # 取余数
print("2 ** 10 =", 2 ** 10)     # 幂运算
