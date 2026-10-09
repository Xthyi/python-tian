#!/bin/zsh
# 双击这个文件 → 输入一句话 → 代码自动推到 GitHub
# 位置：~/Documents/python-practice/提交到GitHub.command

cd "$HOME/Documents/python-practice" || exit 1

echo "════════════════════════════════════"
echo "  提交到 GitHub"
echo "════════════════════════════════════"
echo

# 先看看改了什么
git add -A
echo "本次要提交的文件："
git diff --cached --name-status | sed 's/^/  /'
echo

# 没有改动就别硬提交
if git diff --cached --quiet; then
    echo "⚠️  没有任何改动，跳过提交。"
else
    echo -n "写一句这次做了什么（回车提交，直接回车用默认文案）："
    read msg
    if [ -z "$msg" ]; then
        msg="更新练习"
    fi
    git commit -m "$msg"
    echo
    echo "✅ 已提交：$msg"
fi

echo
echo "正在推送到 GitHub..."
if git push origin main; then
    echo
    echo "🎉 推送成功！"
    echo "   打开看看 → https://github.com/Xthyi/python-tian"
    echo
    echo -n "现在用浏览器打开吗？(y/N)："
    read ans
    if [ "$ans" = "y" ] || [ "$ans" = "Y" ]; then
        open "https://github.com/Xthyi/python-tian"
    fi
else
    echo
    echo "❌ 推送失败。常见原因："
    echo "   · 没网 / GitHub 网页打不开 → 试试手机热点"
    echo "   · SSH 掉了 → 跑一下：ssh -T git@github.com"
    echo "   · 远端有新改动 → 先跑：git pull --rebase origin main"
fi

echo
echo "按任意键关闭..."
read -k 1
