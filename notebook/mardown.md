@[TOC](Markdown中为文字设置颜色, 插入换行和空格)

> 参见: [如何在markdown中设置字体颜色](https://blog.csdn.net/sunshine_lyn/article/details/86476712)
> 

# 为文字设置颜色
Markdown能够解析html文本. 
当需要指定Markdown中个别文字的颜色时,可以插入如下代码, 为指定的文字设置颜色:
```html
<font color="Blue">要设置颜色的文字</font>
```

## 颜色列表
name|display|hex|rgb
-|-|-|-
AliceBlue | <font size="5" color="AliceBlue">■</font> | #F0F8FF | rgb(240, 248, 255)
AntiqueWhite | <font style="font-size:30px;color:AntiqueWhite">■</font> | #FAEBD7 | rgb(250, 235, 215)
Aqua | <font color="Aqua">■</font> | #00FFFF | rgb(0, 255, 255)
Aquamarine | <font color="Aquamarine">■</font> | #7FFFD4 | rgb(127, 255, 212)
Azure | <font color="Azure">■</font> | #F0FFFF | rgb(240, 255, 255)
Beige | <font color="Beige">■</font> | #F5F5DC | rgb(245, 245, 220)
Bisque | <font color="Bisque">■</font> | #FFE4C4 | rgb(255, 228, 196)
Black | <font color="Black">■</font> | #000000 | rgb(0, 0, 0)
BlanchedAlmond | <font color="BlanchedAlmond">■</font> | #FFEBCD | rgb(255, 235, 205)
Blue | <font color="Blue">■</font> | #0000FF | rgb(0, 0, 255)
BlueViolet | <font color="BlueViolet">■</font> | #8A2BE2 | rgb(138, 43, 226)
Brown | <font color="Brown">■</font> | #A52A2A | rgb(165, 42, 42)
BurlyWood | <font color="BurlyWood">■</font> | #DEB887 | rgb(222, 184, 135)
CadetBlue | <font color="CadetBlue">■</font> | #5F9EA0 | rgb(95, 158, 160)
Chartreuse | <font color="Chartreuse">■</font> | #7FFF00 | rgb(127, 255, 0)
Chocolate | <font color="Chocolate">■</font> | #D2691E | rgb(210, 105, 30)
Coral | <font color="Coral">■</font> | #FF7F50 | rgb(255, 127, 80)
CornflowerBlue | <font color="CornflowerBlue">■</font> | #6495ED | rgb(100, 149, 237)
Cornsilk | <font color="Cornsilk">■</font> | #FFF8DC | rgb(255, 248, 220)
Crimson | <font color="Crimson">■</font> | #DC143C | rgb(220, 20, 60)
Cyan | <font color="Cyan">■</font> | #00FFFF | rgb(0, 255, 255)
DarkBlue | <font color="DarkBlue">■</font> | #00008B | rgb(0, 0, 139)
DarkCyan | <font color="DarkCyan">■</font> | #008B8B | rgb(0, 139, 139)
DarkGoldenRod | <font color="DarkGoldenRod">■</font> | #B8860B | rgb(184, 134, 11)
DarkGray | <font color="DarkGray">■</font> | #A9A9A9 | rgb(169, 169, 169)
DarkGreen | <font color="DarkGreen">■</font> | #006400 | rgb(0, 100, 0)
DarkKhaki | <font color="DarkKhaki">■</font> | #BDB76B | rgb(189, 183, 107)
DarkMagenta | <font color="DarkMagenta">■</font> | #8B008B | rgb(139, 0, 139)
DarkOliveGreen | <font color="DarkOliveGreen">■</font> | #556B2F | rgb(85, 107, 47)
Darkorange | <font color="Darkorange">■</font> | #FF8C00 | rgb(255, 140, 0)
DarkOrchid | <font color="DarkOrchid">■</font> | #9932CC | rgb(153, 50, 204)
DarkRed | <font color="DarkRed">■</font> | #8B0000 | rgb(139, 0, 0)
DarkSalmon | <font color="DarkSalmon">■</font> | #E9967A | rgb(233, 150, 122)
DarkSeaGreen | <font color="DarkSeaGreen">■</font> | #8FBC8F | rgb(143, 188, 143)
DarkSlateBlue | <font color="DarkSlateBlue">■</font> | #483D8B | rgb(72, 61, 139)
DarkSlateGray | <font color="DarkSlateGray">■</font> | #2F4F4F | rgb(47, 79, 79)
DarkTurquoise | <font color="DarkTurquoise">■</font> | #00CED1 | rgb(0, 206, 209)
DarkViolet | <font color="DarkViolet">■</font> | #9400D3 | rgb(148, 0, 211)
DeepPink | <font color="DeepPink">■</font> | #FF1493 | rgb(255, 20, 147)
DeepSkyBlue | <font color="DeepSkyBlue">■</font> | #00BFFF | rgb(0, 191, 255)
DimGray | <font color="DimGray">■</font> | #696969 | rgb(105, 105, 105)
DodgerBlue | <font color="DodgerBlue">■</font> | #1E90FF | rgb(30, 144, 255)
Feldspar | <font color="Feldspar">■</font> | #D19275 | rgb(209, 146, 117)
FireBrick | <font color="FireBrick">■</font> | #B22222 | rgb(178, 34, 34)
FloralWhite | <font color="FloralWhite">■</font> | #FFFAF0 | rgb(255, 250, 240)
ForestGreen | <font color="ForestGreen">■</font> | #228B22 | rgb(34, 139, 34)
Fuchsia | <font color="Fuchsia">■</font> | #FF00FF | rgb(255, 0, 255)
Gainsboro | <font color="Gainsboro">■</font> | #DCDCDC | rgb(220, 220, 220)
GhostWhite | <font color="GhostWhite">■</font> | #F8F8FF | rgb(248, 248, 255)
Gold | <font color="Gold">■</font> | #FFD700 | rgb(255, 215, 0)
GoldenRod | <font color="GoldenRod">■</font> | #DAA520 | rgb(218, 165, 32)
Gray | <font color="Gray">■</font> | #808080 | rgb(128, 128, 128)
Green | <font color="Green">■</font> | #008000 | rgb(0, 128, 0)
GreenYellow | <font color="GreenYellow">■</font> | #ADFF2F | rgb(173, 255, 47)
HoneyDew | <font color="HoneyDew">■</font> | #F0FFF0 | rgb(240, 255, 240)
HotPink | <font color="HotPink">■</font> | #FF69B4 | rgb(255, 105, 180)
IndianRed | <font color="IndianRed">■</font> | #CD5C5C | rgb(205, 92, 92)
Indigo | <font color="Indigo">■</font> | #4B0082 | rgb(75, 0, 130)
Ivory | <font color="Ivory">■</font> | #FFFFF0 | rgb(255, 255, 240)
Khaki | <font color="Khaki">■</font> | #F0E68C | rgb(240, 230, 140)
Lavender | <font color="Lavender">■</font> | #E6E6FA | rgb(230, 230, 250)
LavenderBlush | <font color="LavenderBlush">■</font> | #FFF0F5 | rgb(255, 240, 245)
LawnGreen | <font color="LawnGreen">■</font> | #7CFC00 | rgb(124, 252, 0)
LemonChiffon | <font color="LemonChiffon">■</font> | #FFFACD | rgb(255, 250, 205)
LightBlue | <font color="LightBlue">■</font> | #ADD8E6 | rgb(173, 216, 230)
LightCoral | <font color="LightCoral">■</font> | #F08080 | rgb(240, 128, 128)
LightCyan | <font color="LightCyan">■</font> | #E0FFFF | rgb(224, 255, 255)
LightGoldenRodYellow | <font color="LightGoldenRodYellow">■</font> | #FAFAD2 | rgb(250, 250, 210)
LightGrey | <font color="LightGrey">■</font> | #D3D3D3 | rgb(211, 211, 211)
LightGreen | <font color="LightGreen">■</font> | #90EE90 | rgb(144, 238, 144)
LightPink | <font color="LightPink">■</font> | #FFB6C1 | rgb(255, 182, 193)
LightSalmon | <font color="LightSalmon">■</font> | #FFA07A | rgb(255, 160, 122)
LightSeaGreen | <font color="LightSeaGreen">■</font> | #20B2AA | rgb(32, 178, 170)
LightSkyBlue | <font color="LightSkyBlue">■</font> | #87CEFA | rgb(135, 206, 250)
LightSlateBlue | <font color="LightSlateBlue">■</font> | #8470FF | rgb(132, 112, 255)
LightSlateGray | <font color="LightSlateGray">■</font> | #778899 | rgb(119, 136, 153)
LightSteelBlue | <font color="LightSteelBlue">■</font> | #B0C4DE | rgb(176, 196, 222)
LightYellow | <font color="LightYellow">■</font> | #FFFFE0 | rgb(255, 255, 224)
Lime | <font color="Lime">■</font> | #00FF00 | rgb(0, 255, 0)
LimeGreen | <font color="LimeGreen">■</font> | #32CD32 | rgb(50, 205, 50)
Linen | <font color="Linen">■</font> | #FAF0E6 | rgb(250, 240, 230)
Magenta | <font color="Magenta">■</font> | #FF00FF | rgb(255, 0, 255)
Maroon | <font color="Maroon">■</font> | #800000 | rgb(128, 0, 0)
MediumAquaMarine | <font color="MediumAquaMarine">■</font> | #66CDAA | rgb(102, 205, 170)
MediumBlue | <font color="MediumBlue">■</font> | #0000CD | rgb(0, 0, 205)
MediumOrchid | <font color="MediumOrchid">■</font> | #BA55D3 | rgb(186, 85, 211)
MediumPurple | <font color="MediumPurple">■</font> | #9370D8 | rgb(147, 112, 216)
MediumSeaGreen | <font color="MediumSeaGreen">■</font> | #3CB371 | rgb(60, 179, 113)
MediumSlateBlue | <font color="MediumSlateBlue">■</font> | #7B68EE | rgb(123, 104, 238)
MediumSpringGreen | <font color="MediumSpringGreen">■</font> | #00FA9A | rgb(0, 250, 154)
MediumTurquoise | <font color="MediumTurquoise">■</font> | #48D1CC | rgb(72, 209, 204)
MediumVioletRed | <font color="MediumVioletRed">■</font> | #C71585 | rgb(199, 21, 133)
MidnightBlue | <font color="MidnightBlue">■</font> | #191970 | rgb(25, 25, 112)
MintCream | <font color="MintCream">■</font> | #F5FFFA | rgb(245, 255, 250)
MistyRose | <font color="MistyRose">■</font> | #FFE4E1 | rgb(255, 228, 225)
Moccasin | <font color="Moccasin">■</font> | #FFE4B5 | rgb(255, 228, 181)
NavajoWhite | <font color="NavajoWhite">■</font> | #FFDEAD | rgb(255, 222, 173)
Navy | <font color="Navy">■</font> | #000080 | rgb(0, 0, 128)
OldLace | <font color="OldLace">■</font> | #FDF5E6 | rgb(253, 245, 230)
Olive | <font color="Olive">■</font> | #808000 | rgb(128, 128, 0)
OliveDrab | <font color="OliveDrab">■</font> | #6B8E23 | rgb(107, 142, 35)
Orange | <font color="Orange">■</font> | #FFA500 | rgb(255, 165, 0)
OrangeRed | <font color="OrangeRed">■</font> | #FF4500 | rgb(255, 69, 0)
Orchid | <font color="Orchid">■</font> | #DA70D6 | rgb(218, 112, 214)
PaleGoldenRod | <font color="PaleGoldenRod">■</font> | #EEE8AA | rgb(238, 232, 170)
PaleGreen | <font color="PaleGreen">■</font> | #98FB98 | rgb(152, 251, 152)
PaleTurquoise | <font color="PaleTurquoise">■</font> | #AFEEEE | rgb(175, 238, 238)
PaleVioletRed | <font color="PaleVioletRed">■</font> | #D87093 | rgb(216, 112, 147)
PapayaWhip | <font color="PapayaWhip">■</font> | #FFEFD5 | rgb(255, 239, 213)
PeachPuff | <font color="PeachPuff">■</font> | #FFDAB9 | rgb(255, 218, 185)
Peru | <font color="Peru">■</font> | #CD853F | rgb(205, 133, 63)
Pink | <font color="Pink">■</font> | #FFC0CB | rgb(255, 192, 203)
Plum | <font color="Plum">■</font> | #DDA0DD | rgb(221, 160, 221)
PowderBlue | <font color="PowderBlue">■</font> | #B0E0E6 | rgb(176, 224, 230)
Purple | <font color="Purple">■</font> | #800080 | rgb(128, 0, 128)
Red | <font color="Red">■</font> | #FF0000 | rgb(255, 0, 0)
RosyBrown | <font color="RosyBrown">■</font> | #BC8F8F | rgb(188, 143, 143)
RoyalBlue | <font color="RoyalBlue">■</font> | #4169E1 | rgb(65, 105, 225)
SaddleBrown | <font color="SaddleBrown">■</font> | #8B4513 | rgb(139, 69, 19)
Salmon | <font color="Salmon">■</font> | #FA8072 | rgb(250, 128, 114)
SandyBrown | <font color="SandyBrown">■</font> | #F4A460 | rgb(244, 164, 96)
SeaGreen | <font color="SeaGreen">■</font> | #2E8B57 | rgb(46, 139, 87)
SeaShell | <font color="SeaShell">■</font> | #FFF5EE | rgb(255, 245, 238)
Sienna | <font color="Sienna">■</font> | #A0522D | rgb(160, 82, 45)
Silver | <font color="Silver">■</font> | #C0C0C0 | rgb(192, 192, 192)
SkyBlue | <font color="SkyBlue">■</font> | #87CEEB | rgb(135, 206, 235)
SlateBlue | <font color="SlateBlue">■</font> | #6A5ACD | rgb(106, 90, 205)
SlateGray | <font color="SlateGray">■</font> | #708090 | rgb(112, 128, 144)
Snow | <font color="Snow">■</font> | #FFFAFA | rgb(255, 250, 250)
SpringGreen | <font color="SpringGreen">■</font> | #00FF7F | rgb(0, 255, 127)
SteelBlue | <font color="SteelBlue">■</font> | #4682B4 | rgb(70, 130, 180)
Tan | <font color="Tan">■</font> | #D2B48C | rgb(210, 180, 140)
Teal | <font color="Teal">■</font> | #008080 | rgb(0, 128, 128)
Thistle | <font color="Thistle">■</font> | #D8BFD8 | rgb(216, 191, 216)
Tomato | <font color="Tomato">■</font> | #FF6347 | rgb(255, 99, 71)
Turquoise | <font color="Turquoise">■</font> | #40E0D0 | rgb(64, 224, 208)
Violet | <font color="Violet">■</font> | #EE82EE | rgb(238, 130, 238)
VioletRed | <font color="VioletRed">■</font> | #D02090 | rgb(208, 32, 144)
Wheat | <font color="Wheat">■</font> | #F5DEB3 | rgb(245, 222, 179)
White | <font color="White">■</font> | #FFFFFF | rgb(255, 255, 255)
WhiteSmoke | <font color="WhiteSmoke">■</font> | #F5F5F5 | rgb(245, 245, 245)
Yellow | <font color="Yellow">■</font> | #FFFF00 | rgb(255, 255, 0)
YellowGreen | <font color="YellowGreen">■</font> | #9ACD32 | rgb(154, 205, 50)

# 插入换行
在需要换行的文字末尾添加`<br>`,实现换行

# 插入空格
在需要添加空格的文字前添加`&emsp` 或`nbsp;`完成空格的添加.

# 示例

cmake 中if..else的语法:
```md
`if`(\<*condition*\>) <br>
&emsp; &emsp; \<*commands*\> <br>
`elseif`(\<*condition*\>) <font color="forestgreen"># optional block, can be repeated</font> <br>
&emsp; &emsp;\<*commands*\> <br>
`else()`             <font color="forestgreen"># optional block</font> <br>
&emsp; &emsp; \<*commands*\><br>
`endif()`
```

`if`(\<*condition*\>) <br>
&emsp; \<*commands*\> <br>
`elseif`(\<*condition*\>) <font color="forestgreen"># optional block, can be repeated</font> <br>
&emsp; \<*commands*\> <br>
`else()`             <font color="forestgreen"># optional block</font> <br>
&emsp; \<*commands*\><br>
`endif()`
