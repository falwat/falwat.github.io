# Vivado 用户向导 - 综合

> Reference: [ug901-vivado-synthesis.pdf](http://www.xilinx.com/support/documentation/sw_manuals/xilinx2018_3/ug901-vivado-synthesis.pdf)

- [Vivado 用户向导 - 综合](#vivado-用户向导---综合)
  - [Vivado 综合](#vivado-综合)
    - [概述](#概述)
    - [综合方法学](#综合方法学)
    - [Using Synthesis](#using-synthesis)
      - [综合的配置选项](#综合的配置选项)
    - [Running Synthesis](#running-synthesis)

## Vivado 综合

### 概述

"综合"是将RTL描述设计文件转换为门级表示的过程.

支持的RTL描述语言:

- SystemVerilog(IEEE Std 1800-2012)
- Verilog(IEEE Std 1364-2005)
- VHDL(IEEE Std 1076-2002)
- 混合语言(SystemVerilog, Verilog 和 VHDL 的混合)

构建和运行"综合"的两种方法:

- 工程模式(使用IDE配置选项)
- 非工程模式(使用Tcl命令或脚本)

### 综合方法学

### Using Synthesis

#### 综合的配置选项

设计约束的两种类型:

- 物理约束(管脚布局, BRAM, LUT 和 Flip-flops等资源的布局)
- 时序约束

配置项:

- -flatten_hierarchy
  - none
  - full: 除顶层模块外,平面化所有模块;
  - rebuilt

- -bufg: 控制当前设计中可以使用的BUG数量.

- -fanout_limit
  
  扇出数限制.

  > set, reset, clock enable等控制信号不受此开关限制

- -directive: 使用不同的优化策略.
  - Default: 

### Running Synthesis


