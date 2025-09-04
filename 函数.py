def mul(x, *y):
    res = x
    for item in y:
        res = res * item
    return res


# 测试
print("mul(5) =", mul(5))
print("mul(5, 6) =", mul(5, 6))
print("mul(5, 6, 7) =", mul(5, 6, 7))
print("mul(5, 6, 7, 9) =", mul(5, 6, 7, 9))
if mul(5) != 5:
    print("mul(5)测试失败!")
elif mul(5, 6) != 30:
    print("mul(5, 6)测试失败!")
elif mul(5, 6, 7) != 210:
    print("mul(5, 6, 7)测试失败!")
elif mul(5, 6, 7, 9) != 1890:
    print("mul(5, 6, 7, 9)测试失败!")
else:
    try:
        mul()
        print("mul()测试失败!")
    except TypeError:
        print("测试成功!")


# 去除字符串首尾的空格
def trim(s):
    begin = 0
    while begin < len(s) and s[begin] == " ":
        begin += 1
    end = len(s)
    while end > begin and s[end - 1] == " ":
        end -= 1
    return s[begin:end]


# 测试:
if trim("hello  ") != "hello":
    print("测试失败1!")
elif trim("  hello") != "hello":
    print("测试失败2!")
elif trim("  hello  ") != "hello":
    print("测试失败3!")
elif trim("  hello  world  ") != "hello  world":
    print("测试失败4!")
elif trim("") != "":
    print("测试失败5!")
elif trim("    ") != "":
    print("测试失败6!")
else:
    print("测试成功7!")


def findMinAndMax(L):
    return (None, None)


# 测试
if findMinAndMax([]) != (None, None):
    print("测试失败!")
elif findMinAndMax([7]) != (7, 7):
    print("测试失败!")
elif findMinAndMax([7, 1]) != (1, 7):
    print("测试失败!")
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print("测试失败!")
else:
    print("测试成功!")
