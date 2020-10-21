# num 表示生成斐波那契数列的个数
def fibonacci(num):
    # 初始化前两个值
    a = 0
    b = 1
    # 记录每次生成个数的索引
    current_index = 0
    # 循环判断条件是否成立
    while current_index < num:
        result = a
        # 条件成立交换两个变量的值
        a, b = b, a + b
        current_index += 1
        yield result


# 创建生成器
f = fibonacci(1000)

for value in f:
    print(value)

# value = next(f)
#
# print(value)
#
# value = next(f)
#
# print(value)




