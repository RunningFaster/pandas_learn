import numpy as np
import pandas as pd

# 一维对象 Series
s = pd.Series([1, 3, 4, 5, np.nan, 7, 9])
print(s)

# 二维对象 DataFrame
dates = pd.date_range('20200101', periods=6)
print(dates)

df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))
print(df)

df2 = pd.DataFrame({"A": 1,
                    "B": pd.Timestamp('20130102'),
                    'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                    })
print(df2)
print(df2.dtypes)

# 显示头部，限制条数
print(df.head(2))
# 显示尾部，限制条数
print(df.tail(3))
# 显示索引
print(df.index)
# 显示列名
print(df.columns)
# 快速查看数据的统计摘要
print(df.describe())
# 转置数据，索引和列名 切换位置
print(df.T)
# 按轴排序，axis 0表示纵轴，1表示横轴，ascending 表示正序或者倒序
print(df.sort_index(axis=0, ascending=False))
# 按值排序，正序或者倒序
print(df.sort_values(by="B", ascending=False))
# 在 DataFrame 中取出指定的 Series 数据
print(df['A'])
print(df.A)
# 切片，左闭右开
print(df[:2])

# 值包含两种格式：
#   []列表   返回的是 DataFrame
#   具体值   返回的是 对应位置的值

# 根据索引切片，按照时间段进行取值，根据  值进行操作
print(df['2020-01-03':'2020-01-04'])
# 根据标签取值，loc 第一个的值为 横轴的值，第二个值为 纵轴的值，取出的是当前行的 Series，: 表示占位符
print(df.loc[:, :])
# 用值进行切片，注意是 ： 表示 开始值：结束值
print(df.loc['2020-01-03':'2020-01-04', 'A':'C'])
# 取值，第一个值和第二个值都是定值的时候，取出对应的值
print(df.loc['2020-01-03', 'D'])

# 按照整数位置取值，根据 下标进行操作
print(df.iloc[1:2, 3:4])
# 根据下标取值
print(df.iloc[1, 1])

# 布尔索引
print(df[df.A > 0])
# 满足条件的值
print(df[df > 0])
# isin
df2 = df.copy()
df2['E'] = ['one', 'two', 'three', 'four', 'five', 'six']
print(df2)
print(df2[df2['E'].isin(['one', 'three'])])

# 赋值
s1 = pd.Series([1, 2, 3, 4, 5, 6], index=pd.date_range('20200101', periods=6))
print(s1)
# 新增一列
df['F'] = s1
print(df)
# 按标签赋值
df.at[dates[0], 'A'] = 0
print(df)