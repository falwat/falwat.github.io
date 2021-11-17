**目录**

- [Tensorflow Notebook](#tensorflow-notebook)
  - [安装Tensorflow](#安装tensorflow)
  - [保存模型](#保存模型)
  - [Tensorflow Core v2.6.0](#tensorflow-core-v260)
  - [参考](#参考)

---

# Tensorflow Notebook


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
