# Anaconda

- [Anaconda](#anaconda)
  - [设置国内镜像源](#设置国内镜像源)

## 设置国内镜像源

- 在个人目录下查看是否存在`.condarc`文件, 如果不存在, 运行以下命令生成:

```sh
conda config --set show_channel_urls yes
```

- 在`.condarc`中粘贴以下内容:
  
```yaml
channels:
  - defaults
show_channel_urls: true
default_channels:
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/r
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/msys2
custom_channels:
  conda-forge: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  msys2: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  bioconda: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  menpo: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  pytorch: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  simpleitk: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
```

- 运行 `conda clean -i` 清除索引缓存，保证用的是镜像站提供的索引

