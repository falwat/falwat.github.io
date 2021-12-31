>  参见: [The TypeScript Handbook](https://www.typescriptlang.org/docs/handbook/intro.html)

# 1. 概述



# 2. 类型

类型|说明
-|-
any | 任意值. 不做类型检测
boolean | 布尔值
never | 
number | 数值
string | 字符串
void | 空
字面值 | 字面值. 
object | 对象. 

- void
```ts
// 表示函数没有返回值
function fun(): void {
}
```

## 2.1. 字面值
```ts
let gender: "male" | "famale"
```

## 2.2. object
- {PropertyName1: PropertyType, ...}: 限定对象包含的属性
- {..., `PropertyName?`, ...} 表示该属性可有可无
- {[PropertyName: string]: any} 表示可选属性

```ts
let obj: {name: string, age?: number}
obj = {name: "Bob"}
// 错误.
obj = {}
obj = {name: 'Bob', age: 18}
```

## 2.3. array

- `PropertyType[]` PropertyType 的数组
- Array<PropertyType> 同上.

```ts
let a: string[];
```

## 2.4. tuple

- 固定长度的数组.
- `[PropertyType1, PropertyType1, ...]`

```ts
let t1: [stirng, string]
// 枚举
enum Gender {
    Male,
    Female
}

let g: {name: string, gender: Gender};
g = {name: "Bob", gender: Gender.Male};
```

## 2.5. 说明

- `PropertyType1 | PropertyType2` 可以是`PropertyType1` 或 `PropertyType2`
- `&`

# 编译选项
- 将`<tsname>.ts`编译为`<tsname>.js`
```
tsc <tsname>.ts
```
- 监视文件, 文件发生变化时自动编译.
```bash
tsc <tsname>.ts --watch
```
- tsconfig.json
  - 可以使用`tsc --init`自动在当前目录创建`tsconfig.json`
```json
{
    // 编译选项
    "compilerOptions": {
        // 指定编译版本
        "target": "ES2016",
        // 指定使用的模块化规范
        "module": "CommonJS",
        // 指定项目中要使用的库, 一般不需要.
        // "lib": [],
        // 指定编译后文件(.js)存放目录
        "outDir": "./",
        // 将代码合并到一个文件, 一般不使用
        "outFile": "./",
        // 是否编译js文件, 同checkJS一同使用
        "allowJs": false,
        "checkJs": false,
        
    },
    // 
    "include": [],
    // exclude
    "exclude": []
}
```

