# Numpy Notebook

## 导入numpy

```py
import numpy as np
```

## 数据类型转换(astype)

```py
a = np.array([[1,2,3],[4,5,6]])
print(a.dtype)
a.astype('float32')
```

## 多维数组降维

```py
# a.shape = (1, 9)
a = np.ones((1,9))

# b.shape = (9, )
b = a[0, :]
```

## 多维数组增维

```py
# b.shape = (9, )
b = np.ones(9)
# c.shape = (1, 9)
c = b[None, :]
# d.shape = (9, 1)
d = b[:, None]
```