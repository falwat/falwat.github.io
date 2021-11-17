# 流程图(flowchart)

**目录**

- [流程图(flowchart)](#流程图flowchart)
- [基础](#基础)
  - [节点](#节点)
  - [节点形状](#节点形状)
  - [节点间的连接](#节点间的连接)
- [定义样式和类](#定义样式和类)
  - [连接线的样式](#连接线的样式)
- [节点样式](#节点样式)


---

# 基础

## 节点

```mermaid
flowchart
%% 定义一个节点, 节点名(id)是节点的唯一标识
node
%% 带文字的节点, id[text]
node1[带文字的节点]
```

## 节点形状

```
flowchart
    %% 矩形
    N0[矩形]
    N1(圆角矩形)

    %% 圆角矩形, 一般用于"开始"和"结束"节点
    N2([圆角矩形])
    N3[[子程序]]
    N4[(数据库)]
    N5((圆形))
    N6>不对称形状]
    N7{菱形}
    N8{{六边形}}
    N9[/梯形1/]
    N10[\梯形2\]
    N11[/等腰梯形1\]
    N12[\等腰梯形2/]
```

```mermaid
flowchart
    %% 矩形
    N0[矩形]
    N1(圆角矩形)
    %% 圆角矩形, 一般用于"开始"和"结束"节点
    N2([圆角矩形])
    N3[[子程序]]
```

```mermaid
flowchart
    N4[(数据库)]
    N5((圆形))
    N6>不对称形状]
```

```mermaid
flowchart
    N7{菱形}
    N8{{六边形}}
    N9[/梯形1/]
    N10[\梯形2\]
```

```mermaid
flowchart
    N11[/等腰梯形1\]
    N12[\等腰梯形2/]
```

## 节点间的连接

- 线形
  
```mermaid
flowchart
    %% 实线, 最少三个"-", "-"越多线越长
    A1 --- B1
    %% 虚线, 最少一个".", "."越多线越长
    A2 -.- B2
    %% 粗实线, 最少三个"=", "="越多线越长
    A3 === B3
```


- 端点形状
  
```mermaid
flowchart
    %% 线形和端点形状可以任意组合
    %% 双向
    %% 最少两个"-", "-"越多线越长
    A1 <--> B1
    %% 最少一个".", "."越多线越长
    A2 o-.-o B2
    %% 最少两个"=", "="越多线越长
    A3 x==x B3
    %% 单向
    C1 --> D1
    C2 -.-o D2
    C3 ==x D3
```
- 带文字标签(方法一)

```mermaid
flowchart
    %% 前后两边"-"的数量控制相应边线的长度
    C1 --文字--> D1
    %% 前边固定为"-.", 后边"."的数量控制线的长度
    C2 -.文字.-o D2
    %% 前后两边"="的数量控制相应边线的长度
    C3 ==文字==x D3
```

- 带文字标签(方法二)

```mermaid
flowchart LR
    A1 --> |文字|B1
```

- 多节点连接

```mermaid
flowchart LR
    A --> B & C --> D
```

```mermaid
flowchart LR
    A & B --> C & D
```

# 定义样式和类

## 连接线的样式

```mermaid
flowchart LR 
    A --> B --> C --> D
    %% linkStyle <第 Nth 条线> stroke:<线的颜色>,stroke-width:<线宽>,color:<文字颜色>;
    %% 因为连接线没有id, 故只能通过第 Nth 条线的形式指定.
    linkStyle 0 stroke:#0000FF,stroke-width:4px,color:red;
```

# 节点样式

```mermaid
flowchart LR
    id1(Start)-->id2(Stop)
    %% style <id> fill:<背景颜色>,stroke:<边框颜色>,stroke-width:<边框宽度>,color:<文字颜色>,stroke-dasharray:<虚线边框的线段长度和空白长度>
    style id1 fill:#f9f,stroke:#333,stroke-width:4px
    style id2 fill:#bbf,stroke:#f66,stroke-width:2px,color:#fff,stroke-dasharray: 5
```





