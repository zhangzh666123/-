import numpy as np
from sklearn import preprocessing

# 标准化：将数据转换为均值为0，方差为1的数据，即标注正态分布的数据
x = np.array([[1, -1, 2], [2, 0, 0], [0, 1, -1]])
x_scale = preprocessing.scale(x)
print(x_scale.mean(axis=0), x_scale.std(axis=0))

std_scale = preprocessing.StandardScaler().fit(x)
x_std = std_scale.transform(x)
print(x_std.mean(axis=0), x_std.std(axis=0))

# 将数据缩放至给定范围（0-1）
mm_scale = preprocessing.MinMaxScaler()
x_mm = mm_scale.fit_transform(x)
print(x_mm.mean(axis=0), x_mm.std(axis=0))

# 正则化
nor_scale = preprocessing.Normalizer()
x_nor = nor_scale.fit_transform(x)
print(x_nor.mean(axis=0), x_nor.std(axis=0))

# 将分类特征或数据标签转换位独热编码
ohe = preprocessing.OneHotEncoder()
x1 = ([["大象"], ["猴子"], ["老虎"], ["老鼠"]])
x_ohe = ohe.fit(x1).transform([["老虎"]]).toarray()
print(x_ohe)
