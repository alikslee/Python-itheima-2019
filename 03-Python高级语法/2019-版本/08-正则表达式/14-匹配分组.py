# |	匹配左右任意一个表达式
# (ab)	将括号中字符作为一个分组
# \num	引用分组num匹配到的字符串
# (?P<name>)	分组起别名
# (?P=name)	引用别名为name分组匹配到的字符串

import re

# 水果列表
fruit_list = ['apple', 'banana', 'orage', 'pear', 'peach']

for value in fruit_list:
    # 根据每一个字符串，使用正则表达式进行匹配
    # |	匹配左右任意一个表达式
    match_obj = re.match("banana|pear", value)

    if match_obj:
        result = match_obj.group()
        print("我想吃的水果:", result)
    else:
        print("我不想吃的水果:", value)


# 匹配出163、126、qq等邮箱
# \.: 表示对正则表达式里面的.进行了转义，变成了一个普通点，只能匹配.字符
# (163|126|qq) 表示一个分组，出现一个小括号就表示一个分组，分组是从1开始的
# 如果出现多个小括号，分组的顺序是从左到右一次排序
match_obj = re.match("[a-zA-Z0-9_]{4,20}@(163|126|qq)\.com", "hello@163.com")
if match_obj:
    # 获取整个匹配的数据，如果使用分组数的化，默认是0
    result = match_obj.group(0)
    # 获取匹配分组数据
    type = match_obj.group(1)
    print(type)
    print(result)
else:
    print("匹配失败")


# "qq:3014587"
match_obj = re.match("(qq:)([1-9]\d{4,11})", "qq:3014587")
if match_obj:

    result = match_obj.group()
    print(result)

    result = match_obj.group(1)
    print(result)

    result = match_obj.group(2)
    print(result)
else:
    print("匹配失败")

# \num	引用分组num匹配到的字符串
match_obj = re.match("<([a-zA-Z1-6]+)>.*</\\1>", "<html>hh</div>")
if match_obj:

    result = match_obj.group()
    print(result)
else:
    print("匹配失败")


# <html><h1>www.itcast.cn</h1></html>

match_obj = re.match("<(?P<name1>[a-zA-Z1-6]+)><(?P<name2>[a-zA-Z1-6]+)>.*</(?P=name2)></(?P=name1)>", "<html><h1>www.itcast.cn</h1></html>")
if match_obj:

    result = match_obj.group()
    print(result)
else:
    print("匹配失败")
