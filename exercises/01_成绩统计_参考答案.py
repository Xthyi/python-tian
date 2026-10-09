# -*- coding: utf-8 -*-
"""
第 2 课练习参考答案
==================================================
⚠️ 先自己写完 01_成绩统计练习.py 再看这个。

重点不是"答案长什么样"，而是看下面每条"为什么这么写"。
能看懂 ≠ 会写。看完关掉，自己再写一遍。
"""

# --------------------------------------------------
# 第 1 题：列表三件套
# --------------------------------------------------
# 思路：Python 自带 max/min/sum/len，不要自己写循环去比大小

def task1(scores):
    highest = max(scores)
    lowest = min(scores)
    average = round(sum(scores) / len(scores), 1)
    return (highest, lowest, average)

# 为什么用 round？
#   sum/len 出来是 81.66666666666667 这种长尾巴，round(x, 1) 保留 1 位 → 81.7
# 为什么返回括号？
#   return (a, b, c) 返回的是一个"元组"，可以一次性带三个值回来


# --------------------------------------------------
# 第 2 题：字典查最高分的人
# --------------------------------------------------
# 写法一（最像人话，推荐先会这个）

def task2(scores_dict):
    best_name = ""
    best_score = -1
    for name, score in scores_dict.items():   # .items() 一次拿出 (键, 值)
        if score > best_score:
            best_score = score
            best_name = name
    return (best_name, best_score)

# 写法二（一行搞定，等你看懂写法一再用）
#   top = max(scores_dict, key=scores_dict.get)
#   return (top, scores_dict[top])
#
# key=scores_dict.get 的意思是：
#   "比较的时候，别比名字，去比这个名字对应的分数"


# --------------------------------------------------
# 第 3 题：打等级
# --------------------------------------------------
# 关键：从高分往低分判。反过来写会出 bug —— 85 分会先撞上 >=60 被判成"及格"

def task3(score):
    if score >= 90:
        return "优"
    elif score >= 75:
        return "良"
    elif score >= 60:
        return "及格"
    else:
        return "不及格"

# if / elif / else 的规则：从上往下找，找到第一个成立就进，剩下的不看


# --------------------------------------------------
# 三题连起来用（看看函数怎么互相配合）
# --------------------------------------------------

if __name__ == "__main__":
    class_scores = {"小明": 88, "小红": 92, "小刚": 76, "小美": 59}

    numbers = list(class_scores.values())
    print("全班统计：", task1(numbers))

    top_name, top_score = task2(class_scores)
    print(f"最高分是 {top_name}，{top_score} 分，等级：{task3(top_score)}")

    print("\n成绩单：")
    for name, score in class_scores.items():
        print(f"  {name}：{score} 分 → {task3(score)}")
