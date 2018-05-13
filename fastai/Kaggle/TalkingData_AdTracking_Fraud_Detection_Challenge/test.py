import pandas as pd
import dask.dataframe as dd


df = dd.read_csv('train.csv')
print(df.describe().compute())
print(df.info().compute())
# pd.set_option('display.float_format', lambda x: '%.3f' % x)
# t = pd.read_csv('train.csv', usecols=['ip'])
# print(t.describe(include='all'))


chunksize = 10 ** 6
a = pd.Series()
for i in pd.read_csv("train.csv", chunksize=chunksize):

    # a += i.isnull().sum()
    # print(a)
    a = i.describe()
    print(a)

pass

f = pd.read_csv('./train_sample.csv')
print(f.tail())

a = f.info()

b = f.describe()

pass