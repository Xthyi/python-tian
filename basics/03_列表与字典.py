# -*- coding: utf-8 -*-
"""
下一课预习：列表 与 字典
=========================
你今天已经会了：变量 / print / f-string / input / if / while / random。

这节课大概率往这走：容器类型。提前跑一遍，老师在台上讲，你在台下是复习。

运行方式：
    python3 03_预习_列表与字典.py

建议顺序：先原样跑一次看输出，再关掉代码自己默写一遍，最后做文件末尾的练习题。
"""

LINE = "=" * 50


def title(text):
    print()
    print(LINE)
    print(f"  {text}")
    print(LINE)


# ------------------------------------------------------------------
title("1. 列表 list：一串按顺序排队的数据")

scores = [88, 92, 76, 95, 60, 78]

print("原始列表：", scores)
print("长度：", len(scores))
print("第一个：", scores[0], " 最后一个：", scores[-1])
print("前 3 个（切片，左闭右开）：", scores[1:3])

scores.append(100)          # 末尾追加
print("追加 100 后：", scores)

scores.remove(60)           # 按【值】删除
print("删掉 60 后：", scores)

scores.sort()               # 就地排序（从小到大）
print("排序后：", scores)

scores.sort(reverse=True)   # 从大到小
print("倒序后：", scores)

print("最高分：", max(scores), " 最低分：", min(scores), " 平均分：", sum(scores) / len(scores))
print("95 在里面吗？", 95 in scores)
print("班级人数（去重后不同分数个数）：", len(set(scores)))


# ------------------------------------------------------------------
title("2. 用 for 遍历列表（代替手写下标）")

names = ["小明", "小红", "小刚"]

for name in names:
    print(f"  同学：{name}")

print()
for i, name in enumerate(names, start=1):   # 同时拿到序号和值
    print(f"  第 {i} 位：{name}")


# ------------------------------------------------------------------
title("3. 列表推导式：一行顶三行")

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squares = [x * x for x in nums]
evens = [x for x in nums if x % 2 == 0]

print("原数字：", nums)
print("平方：  ", squares)
print("偶数：  ", evens)


# ------------------------------------------------------------------
title("4. 字典 dict：用「名字」而不是「第几个」取数据")

student = {
    "name": "小明",
    "age": 19,
    "major": "软件技术",
    "scores": [88, 92, 76],
}

print("字典整体：", student)
print("取名字：", student["name"])
print("取不存在的键（安全写法）：", student.get("sex", "未填写"))

student["city"] = "杭州"          # 字典里没有这个键 -> 新增
student["age"] = 20               # 已有这个键 -> 覆盖
print("加过城市、改过年龄：", student)

print("所有键：", list(student.keys()))
print("所有值：", list(student.values()))

print()
print("遍历字典（最常用写法）：")
for key, value in student.items():
    print(f"  {key:<8} -> {value}")

print()
print("不存在的键直接取会报错：")
try:
    print(student["height"])
except KeyError as exc:
    print(f"  捕获到 KeyError：{exc}   ← 这就是为什么推荐用 .get()")


# ------------------------------------------------------------------
title("5. 列表 + 字典 组合：真实的「表格」就是这么存的")

classroom = [
    {"name": "小明", "score": 88},
    {"name": "小红", "score": 95},
    {"name": "小刚", "score": 60},
]

print("原始数据：")
for stu in classroom:
    print("  ", stu)

# 求平均分
total = 0
for stu in classroom:
    total += stu["score"]
print("平均分：", round(total / len(classroom), 2))

# 找出最高分
top = classroom[0]
for stu in classroom:
    if stu["score"] > top["score"]:
        top = stu
print("第一名：", top["name"], top["score"])

# 排序：按分数从高到低
ranked = sorted(classroom, key=lambda s: s["score"], reverse=True)
print("排行榜：")
for i, stu in enumerate(ranked, start=1):
    print(f"  {i}. {stu['name']}  {stu['score']}")


# ------------------------------------------------------------------
title("6. 函数：把一段逻辑打包，重复用")

def average(numbers):
    """返回平均值；空列表返回 0，避免除以 0 崩溃。"""
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


def level(score):
    """分数转等级。"""
    if score >= 90:
        return "优"
    if score >= 80:
        return "良"
    if score >= 60:
        return "及格"
    return "不及格"


print("给 [88, 92, 76] 求平均：", average([88, 92, 76]))
print("空列表求平均（不崩溃）：", average([]))

print()
for stu in classroom:
    print(f"  {stu['name']}  {stu['score']} 分  ->  {level(stu['score'])}")


# ------------------------------------------------------------------
title("7. 综合：把上面全用上，写一个成绩统计器")

def report(students):
    """打印一份完整的成绩报告。"""
    print("  " + "-" * 42)
    print(f"  {'姓名':<8}{'分数':>6}   {'等级':<6}")
    print("  " + "-" * 42)

    for stu in sorted(students, key=lambda s: s["score"], reverse=True):
        print(f"  {stu['name']:<8}{stu['score']:>6}   {level(stu['score']):<6}")

    print("  " + "-" * 42)
    scores = [s["score"] for s in students]
    print(f"  人数 {len(scores)}   平均 {average(scores):.1f}   最高 {max(scores)}   最低 {min(scores)}")
    print("  " + "-" * 42)


report(classroom)


# ------------------------------------------------------------------
title("课后练习（自己写，写完跑一遍看对不对）")

print("""
  ① 让别人录入 5 个数字，存进列表，输出最大值、最小值、平均值。
     （提示：input 循环 5 次 + append）

  ② 把 "apple,banana,orange" 用 split 切成列表，再转成大写输出。
     （提示："a,b".split(",") 得到列表；s.upper()）

  ③ 用字典存一个「通讯录」：3 个人的名字 -> 电话。
     输入一个名字，输出对应电话；查不到就提示「查无此人」。
     （提示：用 .get() 而不是 []）

  ④ 综合：把上面 03 里 classroom 那段改成函数，让老师随便加人，
     输入 "小明 88" 这样的字符串就能录入，最后打印排行榜。
     （提示：input().split() 拆名字和分数）

  写完就存成 04_exercises.py，然后 git 提交一次。
""")

print(LINE)
print("  预习完成。上课时老师讲到这里，你已经跑过一遍了。")
print(LINE)
