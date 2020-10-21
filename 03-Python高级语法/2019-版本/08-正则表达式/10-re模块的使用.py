import re

# 根据正则表达式匹配数据
# 1. 正则表达式
# 2. 要匹配的字符串
# 3. 返回匹配对象
match_obj = re.match("hel", "hello")
# 获取匹配结果
result = match_obj.group()
print(result)