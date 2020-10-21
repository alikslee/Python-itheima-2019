# 生成器：根据程序员指定的算法规则循环生成数据，当条件不成立时生成数据就结束，提示：不是一次性把所有数据全部生成出来
# 而是使用一次生成一次，这样可以节省大量的内存空间。

# 生成器的创建有两种方式

# 1. 生成器推导式，把列表推导式中的中括号改成小括号即可
# 2. yield关键字，只要在函数里面看到有yield那么这个函数可以任务是一个生成器


# 创建了生成器
my_generator = (value * 2 for value in range(3))
print(my_generator)

# 生成器取值使用next函数获取生成器中的下一个值
# value = next(my_generator)
# print(value)
# value = next(my_generator)
# print(value)
# value = next(my_generator)
# print(value)
# 当生成器已经没有值时，会抛出StopIteration，表示生成器生成数据完毕
# value = next(my_generator)
# print(value)
#
# while True:
#     try:
#         value = next(my_generator)
#         print(value)
#     except Exception as e:
#         break # 跳出循环表示取值完成

# for循环内部循环调用next函数获取生成器中的下一值，当出现异常for循环内部自动进行了异常捕获。
for value in my_generator:
    print(value)