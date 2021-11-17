# Numpy Notebook



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