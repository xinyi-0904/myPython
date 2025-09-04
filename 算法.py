"""
汉诺塔问题
首先是将A柱最上方的n-1个圆盘落在B柱，将此时A柱的最小圆盘落在C柱，B柱上的n-1个圆盘，落在C柱。
"""


def move(n, a, b, c):
    if n == 1:
        print(a, "-->", c)
    else:
        move(n - 1, a, c, b)
        move(1, a, b, c)
        move(n - 1, b, a, c)


move(3, "A", "B", "C")


"""
去除字符串首尾的空格（切片）
"""


def trim(s):
    begin = 0
    while begin < len(s) and s[begin] == " ":
        begin += 1
    end = len(s)
    while end > begin and s[end - 1] == " ":
        end -= 1
    return s[begin:end]
