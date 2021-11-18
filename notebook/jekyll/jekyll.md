# jekyll

## Quickstart

> 参考: [Quickstart](https://jekyllrb.com/docs/)

Jekyll是一个静态站点生成器. 它将你用标记语言编写的文本,使用布局来创建一个静态网站。您可以调整站点的外观和感觉、url、页面上显示的数据等等.

- 安装 jekyll 和 bundler

```sh
gem install jekyll bundler
```

- 创建新的jekyll站点

```sh
jekyll new myblog
```

- 切换至站点目录

```
cd myblog
```

- 在本地运行站点

```sh
bundle exec jekyll serve
```

- 浏览[http://localhost:4000](http://localhost:4000)

## 安装

> 参考: [installation](https://jekyllrb.com/docs/installation/)



> 参考: [Command Line Usage](https://jekyllrb.com/docs/usage/) 

## 在Windows上安装Jekyll

> 参考: [Jekyll on Windows](https://jekyllrb.com/docs/installation/windows/)

### Installing Ruby and Jekyll

...

### Installation via Bash on Windows 10

- 打开`wsl`

```sh
sudo apt-get update -y && sudo apt-get upgrade -y
```

- 安装ruby
  
```sh
sudo apt-add-repository ppa:brightbox/ruby-ng
sudo apt-get update
sudo apt-get install ruby2.5 ruby2.5-dev build-essential dh-autoreconf
```

- 更新 Ruby gems

```sh
gem update
```
- 安装 Jekyll

```sh
sudo gem install jekyll bundler
```

- 测试

```sh
jekyll -v
```
