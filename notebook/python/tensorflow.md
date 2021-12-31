**目录**

- [Tensorflow Notebook](#tensorflow-notebook)
  - [基础知识](#基础知识)
    - [张量(tensor)](#张量tensor)
  - [安装Tensorflow](#安装tensorflow)
  - [保存模型](#保存模型)
  - [Tensorflow Core v2.6.0](#tensorflow-core-v260)
  - [参考](#参考)

---

# Tensorflow Notebook

## 基础知识

### 张量(tensor)

> 参考: [张量简介](https://tensorflow.google.cn/guide/tensor?hl=zh_cn)

张量是具有统一类型（称为 dtype）的多维数组。

标量为"0秩"张量,向量为"1秩"张量, 矩阵为"2秩"张量

```py
# 标量
rank_0_tensor = tf.constant(4)
# 向量
rank_1_tensor = tf.constant([2.0, 3.0, 4.0])

# 矩阵
rank_2_tensor = tf.constant([[1, 2],
                             [3, 4],
                             [5, 6]], dtype=tf.float16)
```

张量转换为numpy数组:
```py
# [1]
numpy.array(tensor)
# [2]
tensor.numpy()
```

特殊类型张量:

- 不规则张量
- 稀疏张量

张量的基本数学运算

```py
a = tf.constant([[1, 2],
                 [3, 4]])
b = tf.constant([[1, 1],
                 [1, 1]]) # Could have also said `tf.ones([2,2])`

# 元素加
a + b # tf.add(a, b)
# 元素减
a - b # tf.subtract(a, b)
# 元素乘
a * b # tf.multiply(a, b)
# 矩阵乘
a @ b # tf.matmul(a, b)
```

张量相关的几个术语

- 形状(Tensor.shape)
- 秩(tensorflow.rank)
- 轴/维度(Tensor.ndim)
- 大小(tensorflow.size): 张量的总项数，即乘积形状向量

典型轴顺序

![shape2.png](./images/shape2.png)

## 安装Tensorflow

- 确认已安装`Anaconda`
- 确认已配置[国内镜像源](./anaconda.md/#设置国内镜像源)
- 创建虚拟环境并安装tensorflow
  ```
  conda create -n tf tensorflow
  ```

## 保存模型

> 参考: [训练检查点](https://tensorflow.google.cn/guide/checkpoint?hl=zh_cn)

## Tensorflow Core v2.6.0

- [tf](https://tensorflow.google.cn/versions/r2.6/api_docs/python/tf?hl=zh_cn) 
  - [keras](https://tensorflow.google.cn/versions/r2.6/api_docs/python/tf/keras?hl=zh_cn)
    - [optimizers](https://tensorflow.google.cn/versions/r2.6/api_docs/python/tf/keras/optimizers?hl=zh_cn)
  - [train](https://tensorflow.google.cn/versions/r2.6/api_docs/python/tf/train?hl=zh_cn)
    - [tf.train.Checkpoint](https://tensorflow.google.cn/versions/r2.6/api_docs/python/tf/train/Checkpoint?hl=zh_cn): 保存和恢复检查点



## 参考
- [Tensorflow 指南](https://tensorflow.google.cn/guide?hl=zh_cn)
- [github](https://github.com/tensorflow/tensorflow/tree/v2.6.0)
