# *	匹配前一个字符出现0次或者无限次，即可有可无
# +	匹配前一个字符出现1次或者无限次，即至少有1次
# ?	匹配前一个字符出现1次或者0次，即要么有1次，要么没有
# {m}	匹配前一个字符出现m次
# {m,n}	匹配前一个字符出现从m到n次
import re

# 1. 正则表达式
# 2. 要匹配的字符串
# *	匹配前一个字符出现0次或者无限次，即可有可无
match_obj = re.match("t.*o", "to")
if match_obj:
    # 获取匹配结果
    result = match_obj.group()
    print(result)
else:
    print("匹配失败")

# + 匹配前一个字符串至少出现一次
match_obj = re.match("t.+o", "trsdfo")
if match_obj:
    # 获取匹配结果
    result = match_obj.group()
    print(result)
else:
    print("匹配失败")

# ?: 匹配前一个字符串出现0次或者1次
match_obj = re.match("https?", "http")
if match_obj:
    # 获取匹配结果
    result = match_obj.group()
    print(result)
else:
    print("匹配失败")

# {m}: 匹配前一个字符串必须出现m次
match_obj = re.match("ht{2}p", "http")
if match_obj:
    # 获取匹配结果
    result = match_obj.group()
    print(result)
else:
    print("匹配失败")

# {m, n}： 匹配前一个字符串最少出现m次，最多出现n次
match_obj = re.match("ht{1,3}p", "httttp")
if match_obj:
    # 获取匹配结果
    result = match_obj.group()
    print(result)
else:
    print("匹配失败")

# 扩展： {m, }:匹配前一个字符串至少出现m次
match_obj = re.match("ht{2,}p", "htttttp")
if match_obj:
    # 获取匹配结果
    result = match_obj.group()
    print(result)
else:
    print("匹配失败")