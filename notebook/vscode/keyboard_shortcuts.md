# VSCode 常用快捷键

## 查看快捷键设置

- 菜单: File | Preferences | Keyboard Shortcuts
- 快捷键: `Ctrl+K Ctrl+S`
- 按钮: 左下角管理图标

## 常用快捷键

### 编辑

命令| 按键绑定 | 条件
-|-|-
复制 | `Ctrl + C` | -
向下复制一行 | `Shift + Alt + downArrow`  | 编辑状态 & !只读
向上复制一行 | `Shift + Alt + upArrow` | 编辑状态 & !只读
删除整行 | `ctrl+shift+k` | textInputFocus && !editorReadonly


### 光标

命令| 按键绑定 | 条件
-|-|-
在上一行添加光标 | `Ctrl + Alt + upArrow` | 编辑状态
在下一行添加光标 | `Ctrl + Alt + downArrow` | 编辑状态
光标重做 | `Ctrl + U` | 编辑状态
对下一个匹配项添加选择 | `Ctrl + D` | 编辑状态


### 调试

命令| 按键绑定 | 条件
-|-|-
调试: 启动调试 | `F5` | debuggersAvailable && debugState == 'inactive'
调试: 运行 | `Ctrl + F5` | debuggersAvailable && debugState != 'initializing'
调试: 继续 | `F5` | debugState == 'stopped'
调试: 暂停 | `F6` | debugState == 'running'
调试: 切换断点 | `F9` | debuggersAvailable && editorTextFocus
调试: 单步 | `F10` | debugState == 'stopped'    
调试: 步入 | `F11`| debugState != 'inactive'
调试: 步出 | `Shift + F11` | debugState == 'stopped'    

### 视图
命令| 按键绑定 | 条件
-|-|-
快速切换当前组中上一个编辑器 | `ctrl+tab` | -
关闭所有编辑器 | `ctrl+k ctrl+w` | -
关闭编辑器 | `ctrl+w`
显示文件浏览器(explorer)| `ctrl+shift+e`
视图放大 | `ctrl + =` <br> `ctrl + shift + =` <br> `ctrl+ numpad_add`
视图缩小 | `ctrl + -` <br> `ctrl + shift +  -` <br> `ctrl+numpad_subtract`
视图还原 | `Ctrl + numpad0`
切换侧边栏显示| `ctrl + b`
切换面板显示 | `ctrl + j`
聚焦到侧边栏 | `Ctrl+0`
聚焦到第(1,2,...,8)个分组 | `Ctrl + [1,2,...,8]`
切换下一个编辑器 | `Ctrl + pageDown`
切换上一个编辑器 | `Ctrl + pageUp`
快速打开先前的编辑器| `Ctrl + Tab`
快速打开视图| `Ctrl + Q`
分割编辑器编辑器 | `Ctrl + \`
跳转到括号 | `Ctrl + shift + \`


 


### 窗口

命令| 按键绑定 | 条件
-|-|-
关闭窗口 | `Ctrl + Shift + W` <br> `Alt+ F4` | -





 key | Ctrl+ | Ctrl+Shift+ | Alt+ | Alt + Shift+ | Ctrl + Alt + Shift+ | Ctrl+K, 
-|-|-|-|-|-|-
Tab | 快速切换当前组中上一个编辑器 | 同`Ctrl` | 系统使用 | 系统使用 | 与`Alt + Shift`相同 | -
Q | - |
B | 切换侧边栏显示 | - | - | - | - | -
\ | 拆分编辑器 | 添加


