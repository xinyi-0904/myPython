from functools import reduce


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
    if not L:
        return (None, None)
    min = L[0]
    max = L[0]
    for item in L:
        if item < min:
            min = item
        elif item > max:
            max = item
    return (min, max)


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
    print("最大值最小值检查测试成功!")

L1 = ["Hello", "World", 18, "Apple", None]
L2 = [x.lower() for x in L1 if isinstance(x, str)]

# 测试:
print(L2)
if L2 == ["hello", "world", "apple"]:
    print("测试返回字符串通过!")
else:
    print("测试失败!")

g = (x * x for x in range(10))
for n in g:
    print(n)


def add(x, y, f):
    return f(x) + f(y)


print(add(-5, 6, abs))

# 高阶函数
## map和reduce

"""
利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
"""


def normalize(name):
    return name.capitalize()
    pass


# 测试:
L1 = ["adam", "LISA", "barT"]
L2 = list(map(normalize, L1))
print(L2)

"""
请编写一个prod()函数，可以接受一个list并利用reduce()求积
"""


def compute(x, y):
    return x * y


def prod(L):
    return reduce(compute, L)


print("3 * 5 * 7 * 9 =", prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print("测试成功!")
else:
    print("测试失败!")


"""
利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456
"""

# DIGITS = {
#     "0": 0,
#     "1": 1,
#     "2": 2,
#     "3": 3,
#     "4": 4,
#     "5": 5,
#     "6": 6,
#     "7": 7,
#     "8": 8,
#     "9": 9,
# }


# def str2float(s):
#     def compute(s):
#         def fn(x, y):
#             return x * 10 + y

#         def char2num(s):
#             return DIGITS[s]

#         return reduce(fn, map(char2num, s))

#     result = list(map(compute, s.split(".")))
#     return result[0] + result[1] * 0.001


# 方法2
def char2num(s):
    return {
        "0": 0,
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
    }[s]


def str2float(s):
    # 移除小数点，记录小数位数
    if "." in s:
        integer_str, decimal_str = s.split(".")
        decimal_digits = len(decimal_str)
        num_str = integer_str + decimal_str
    else:
        num_str = s
        decimal_digits = 0

    # 转换为数字
    num = reduce(lambda x, y: x * 10 + y, map(char2num, num_str))

    # 调整小数位
    return num / (10**decimal_digits)


print("str2float('123.456') =", str2float("123.456"))
if abs(str2float("123.456") - 123.456) < 0.00001:
    print("测试成功!")
else:
    print("测试失败!")
