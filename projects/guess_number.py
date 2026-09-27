# -*- coding: utf-8 -*-
"""
猜数字小游戏 —— 综合练习 input / while / if / random

运行方式：
    python3 projects/guess_number.py
"""

import random

print("=" * 40)
print("  猜数字游戏（1 ~ 100）")
print("=" * 40)

answer = random.randint(1, 100)   # 随机生成答案
count = 0                          # 记录猜了几次

while True:
    guess_text = input("请输入你猜的数字（直接回车退出）：").strip()

    if guess_text == "":
        print(f"退出游戏。答案是 {answer}。")
        break

    # 用户输入的是字符串，要转成整数才能比较
    if not guess_text.isdigit():
        print("请输入正整数哦～")
        continue

    guess = int(guess_text)
    count += 1

    if guess < answer:
        print("太小了，往大猜 ⬆️")
    elif guess > answer:
        print("太大了，往小猜 ⬇️")
    else:
        print(f"🎉 猜对了！答案就是 {answer}，你一共猜了 {count} 次。")
        break
