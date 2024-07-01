# Mirzam

一个简单的在AWD比赛中批量提交flag的小工具

## 使用

运行需要python3及requests库  
首先按实际需要修改`mirzam.py`，具体请参照注释说明  
然后有下面三种用法  

### API

1. 将修改完毕的`mirzam.py`和攻击脚本置于同一目录下
2. 在攻击脚本中调用

~~~python
from mirzam import mirzam
...
# 这里是一段拿flag的代码
...
# 上分时间到！
mirzam(flag)
# 如果需要失败结果回显的话……
m = mirzam(flag)
if m:
    print(m)
~~~

### 命令行

~~俗称手动档~~  
运行`cli.py`，在命令行界面批量粘贴flag，一行一flag，连续按两次回车开始提交  

### 从文件读取

打开`from_file.py`调整flag文件路径（默认为`flag.txt`），然后直接运行  
flag文件里面也是一行一flag的格式  

## 测试

修改完`mirzam.py`之后总得测试一下吧  
或者你只是想简单（？）地提交一个flag  
~~~bash
python mirzam.py flag{114514}
~~~

## 例子

> 假设我们已经在其他目标服务器种好了一批不死马  
> 接下来只要批量使用不死马提供的后门获取flag就能狠狠地上分了！  

具体实现请参看`attack_example.py`

## 其他

如果有问题和意见，欢迎提issue :)  

> 无用小知识：项目名来源于一颗恒星 —— 军市一（大犬座β）
