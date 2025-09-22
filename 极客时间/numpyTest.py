import numpy as np

a1 = np.array([1, 2, 3])
b1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
b1[1, 1] = 10
# 通过函数shape属性获得数组的大小
print(a1.shape)
print(b1.shape)
# 通过dtype获得元素的属性
print(a1.dtype)
print(b1)

# 通过 dtype 定义结构体类型，在定义数组时用array 中指定了结构数组的类型 dtype=persontype
persontype = np.dtype(
    {
        "names": ["name", "age", "chinese", "math", "english"],
        "formats": ["S32", "i", "i", "i", "f"],
    }
)
peoples = np.array(
    [
        ("ZhangFei", 32, 75, 100, 90),
        ("GuanYu", 24, 85, 96, 88.5),
        ("ZhaoYun", 28, 85, 92, 96.5),
        ("HuangZhong", 29, 65, 85, 100),
    ],
    dtype=persontype,
)
ages = peoples[:]["age"]
chineses = peoples[:]["chinese"]
maths = peoples[:]["math"]
englishs = peoples[:]["english"]
# 平均年龄
print(np.mean(ages))

# 等差数组的创建
# 通过指定初始值、终值、步长来创建等差数列的一维数组，默认是不包括终值的。
x1 = np.arange(1, 11, 2)
# 通过指定初始值、终值、元素个数来创建等差数列的一维数组，默认是包括终值的。
x2 = np.linspace(1, 9, 5)
# 加法
print(np.add(x1, x2))
# 减法
print(np.subtract(x1, x2))
# 乘法
print(np.multiply(x1, x2))
# 除法
print(np.divide(x1, x2))
# n次方，x1为基数，x2 为次方数
print(np.power(x1, x2))
# 取余数
print(np.remainder(x1, x2))

# 计算数组/矩阵中的最大值，最小值
a2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(np.amin(a2))
# 沿着行方向的最小值，所有元素都往第一行坍塌
print(np.amin(a2, 0))
# 沿着列方向的最小值，所有元素都往第一列坍塌
print(np.amin(a2, 1))
# 计算最大值与最小值的差
print(np.ptp(a2))
print(np.ptp(a2, 0))
print(np.ptp(a2, 1))

# 统计数组的百分位数
print(np.percentile(a2, 50))
print(np.percentile(a2, 50, axis=0))
print(np.percentile(a2, 50, axis=1))
# 统计数组的中位数
print(np.median(a2))
print(np.median(a2, axis=0))
print(np.median(a2, axis=1))
# 统计数组的平均数
print(np.mean(a2))
print(np.mean(a2, axis=0))
print(np.mean(a2, axis=1))
# percentile() 代表着第 p 个百分位数，这里 p 的取值范围是 0-100，如果 p=0，那么就是求最小值，如果 p=50 就是求平均值，如果 p=100 就是求最大值。

# 统计数组中的加权平均值
a3 = np.array([1, 2, 3, 4])
wts = np.array([1, 2, 3, 4])
print(np.average(a3))
# np.average(a,weights=wts)=(1*1+2*2+3*3+4*4)/(1+2+3+4)=3.0
print(np.average(a3, weights=wts))
# 标准差和方差
print(np.std(a3))
print(np.var(a3))

# 排序
a = np.array([[4, 3, 2], [2, 4, 1]])
print("=====排序=====")
print(np.sort(a))  # 默认按最后一个轴排序（axis=-1）
print(np.sort(a, axis=None))  # 将数组展平后排序
print(np.sort(a, axis=0))  # 沿着行方向（垂直）排序
print(np.sort(a, axis=1))  # 沿着列方向（水平）排序
