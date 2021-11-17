# Github Pages

## 安装Jekyll



> 参考: [github pages](https://pages.github.com/)

## 创建仓库

> 参考: [Quickstart for GitHub Pages](https://docs.github.com/en/pages/quickstart)

在 [GitHub](https://github.com) 上创建`<username>.github.io`的仓库. `username`为你自己的用户名.



## 克隆到本地

```sh
git clone https://github.com/falwat/falwat.github.io.git
```

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
## Creating a GitHub Pages site with Jekyll

> 参考: [Creating a GitHub Pages site with Jekyll](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/creating-a-github-pages-site-with-jekyll)



## Testing your GitHub Pages site locally with Jekyll

- [安装Jekyll](#在windows上安装jekyll)
- 