# ^	匹配字符串开头
# $	匹配字符串结尾

import re

# 1. 正则表达式
# 2. 要匹配的字符串
match_obj = re.match("^\d.*", "1abc")
if match_obj:
    # 获取匹配结果
    result = match_obj.group()
    print(result)
else:
    print("匹配失败")


# 1. 正则表达式
# 2. 要匹配的字符串
match_obj = re.match(".*\d$", "aa3")
if match_obj:
    # 获取匹配结果
    result = match_obj.group()
    print(result)
else:
    print("匹配失败")


# 1. 正则表达式
# 2. 要匹配的字符串
match_obj = re.match("^\d.*\d$", "2asdfa3")
if match_obj:
    # 获取匹配结果
    result = match_obj.group()
    print(result)
else:
    print("匹配失败")

# [^指定字符] 表示除了指定字符都匹配

# [^47] 除了4和7都匹配
# ^: 表示以指定字符串开头
# [^]: 表示除了指定字符串都匹配
match_obj = re.match("^\d.*[^47]$", "2asdfaa")
if match_obj:
    # 获取匹配结果
    result = match_obj.group()
    print(result)
else:
    print("匹配失败")