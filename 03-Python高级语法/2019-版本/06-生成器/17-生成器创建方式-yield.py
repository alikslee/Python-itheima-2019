# 在函数里面看到有yield关键字，那么这个函数就是生成器了
def my_generator():
    for i in range(3):
        print("开始生成数据啦...")
        # 当程序执行到yield关键字的时候代码暂停并把结果返回，再次启动生成器的时候会在暂停的位置继续往下执行
        yield i
        print("上一次的数据生成完了...")


result = my_generator()
print(result)

# 获取生成器下一个值

value = next(result)
print(value)

# value = next(result)
# print(value)
#
# value = next(result)
# print(value)
#
# value = next(result)
# print(value)

# 生成器把所有数据生成完毕后，再次其它生成器会抛出一个StopIteration异常
# for value in result:
#     print(value)