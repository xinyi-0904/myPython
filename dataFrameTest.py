import pandas as pd
from pandas import Series, DataFrame
from pandasql import sqldf, load_meat, load_births
import numpy as np

data = {
    "Chinese": [66, 95, 93, 90, 90],
    "English": [65, 85, 92, 88, 88],
    "Math": [30, 98, 96, 77, 77],
}
df1 = DataFrame(data)
df2 = DataFrame(
    data,
    index=["ZhangFei", "GuanYu", "ZhaoYun", "HuangZhong", "DianWei"],
    columns=["English", "Math", "Chinese"],
)
print(df1)
# print(df2)

# 数据清洗
# 1.删除不必要的列/行
df2 = df2.drop(columns=["Chinese"])
df2 = df2.drop(index=["ZhangFei"])
# print(df2)

# 2.重命名列名
df2.rename(columns={"English": "yingyu"}, inplace=True)
# print(df2)

# 3.去掉重复的行
df1 = df1.drop_duplicates()
# print(df1)

# 4.更改数据格式
df2["yingyu"] = df2["yingyu"].astype("str")

# 5.删除空格
df3 = pd.DataFrame({"English": [None, "world ", "  python", 123, "  %  "]})
# print(df3)
df3["English"] = df3["English"].astype("str").map(str.strip)
# print(df3)
# 删除特殊符号
df3["English"] = df3["English"].str.strip("%")
# print(df3)

# 6.大小写转换
# 全部大写
df3.columns = df3.columns.str.upper()
# 全部小写
df3.columns = df3.columns.str.lower()
# 首字母大写
df3.columns = df3.columns.str.title()
# print(df3)
# print(df3.isnull())  # 前提没被转换为字符串
# print(df3.isnull().any())

# 7.使用apply函数对数据清洗
# 对值进行大写转换
df4 = pd.DataFrame({"english": ["hello", "world ", "  python", "we", "qw"]})
df4["english"] = df4["english"].apply(str.upper)
# print(df4)
# 对值进行函数处理
df5 = pd.DataFrame({"English": [11, 22, 33, 44, 55], "Chinese": [66, 95, 93, 90, 90]})


def double_df(x):
    return 2 * x


df5["English"] = df5["English"].apply(double_df)
# print(df5)


def plus(df, n, m):
    df["new1"] = (df["Chinese"] + df["English"]) * m
    df["new2"] = (df["Chinese"] + df["English"]) * n
    return df


df5 = df5.apply(
    plus,
    axis=1,
    args=(
        2,
        3,
    ),
)
# print(df5)

# print(df5.describe())

# 8.使用 sql 语句
pysqldf = lambda sql: sqldf(sql, globals())
sql = "select * from df1 where Chinese ='66'"
print(pysqldf(sql))
