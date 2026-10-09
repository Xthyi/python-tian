# -*- coding: utf-8 -*-
"""
课堂环境自检 —— 进教室坐下先跑一遍，5 秒确认电脑能正常上课。

运行方式（终端里）：
    cd ~/WorkBuddy/2026-10-09-10-43-23/课堂提速包
    python3 01_环境自检.py
"""

import os
import platform
import shutil
import subprocess
import sys

LINE = "=" * 48
fails = []


def row(name, ok, detail=""):
    print(f"{'✅' if ok else '❌'} {name:<8} {detail}")
    return ok


print(LINE)
print("  课堂环境自检")
print(LINE)

# 1. Python 本体
ver = sys.version.split()[0]
py_ok = sys.version_info >= (3, 10)
row("Python", py_ok, f"{ver}   {sys.executable}")
if not py_ok:
    fails.append("Python 版本偏低，建议 3.10 及以上")

# 2. 系统信息（老师问起来能直接答）
row(
    "系统",
    True,
    f"{platform.system()} {platform.mac_ver()[0] or platform.release()} / {platform.machine()}",
)

# 3. Git（期末交作品集全靠它）
git = shutil.which("git")
if git:
    try:
        gv = subprocess.run(
            [git, "--version"], capture_output=True, text=True, timeout=5
        ).stdout.strip()
    except Exception:
        gv = "git 可用"
    row("Git", True, gv)
else:
    row("Git", False, "没找到，终端跑：xcode-select --install")
    fails.append("Git 不可用，无法做版本记录")

# 4. 中文与编码
row("中文", True, "你好，Python —— 中文输出正常")

# 5. 当前目录是否可写（防止上课写了代码存不上）
here = os.path.dirname(os.path.abspath(__file__))
try:
    probe = os.path.join(here, ".write_probe")
    with open(probe, "w", encoding="utf-8") as f:
        f.write("ok")
    os.remove(probe)
    row("可写", True, here)
except Exception as exc:  # noqa: BLE001
    row("可写", False, f"{here}  ->  {exc}")
    fails.append("当前目录不可写，换到 Documents 下再试")

# 6. 课堂要用的三个核心模块能不能导入
bad = []
for mod in ("random", "json", "datetime"):
    try:
        __import__(mod)
    except ImportError:
        bad.append(mod)
row("标准库", not bad, "random / json / datetime 就绪" if not bad else f"缺失：{bad}")
if bad:
    fails.append(f"标准库缺失：{bad}")

print("-" * 48)
if fails:
    print(f"⚠️  有 {len(fails)} 项要处理：")
    for item in fails:
        print(f"    · {item}")
else:
    print("🎉 全绿，随时可以开讲。")

print(LINE)
print("下一步：打开 02_课堂速查卡.md 放在旁边，老师讲到哪查到哪。")
print(LINE)
