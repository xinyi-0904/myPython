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


"""
生成所有素数
惰性求值的威力：我们不需要预先计算所有数字，只在需要的时候才计算下一个，而且计算过程中会自动应用所有已有的过滤规则
"""


def _not_divisible(n):
    print(f"创建过滤器：过滤掉能被 {n} 整除的数")
    return lambda x: x % n > 0


def _odd_iter():
    n = 1
    while True:
        n = n + 2
        print(f"生成奇数：{n}")
        yield n


def primes():
    yield 2
    print("开始质数生成，初始序列为奇数序列")
    it = _odd_iter()  # 初始序列
    while True:
        n = next(it)  # 返回序列的第一个数
        print(f"找到质数：{n}")
        yield n
        print(f"为质数 {n} 创建过滤器...")
        it = filter(_not_divisible(n), it)  # 构造新序列


print("开始生成前5个质数:")
p = primes()
for i in range(5):
    result = next(p)
    print(f"第{i+1}个质数: {result}")
    print("-" * 30)
