import copy
# 浅拷贝: 只会对可变类型的第一层对象进行拷贝，不会对子对象进行拷贝，
# 拷贝成功后会开辟一个新的内存空间存储拷贝这个对象

# 不可变类型：　数字、字符串、元组

num1 = 1
# copy() 表示是一个浅拷贝函数
# 浅拷贝
num2 = copy.copy(num1)
# 查看后内存地址没有发生变化，说明没有对对象进行拷贝，也就说没有开辟新的内存空间
print("num1:", id(num1), "num2:", id(num2))
# 对于不可变类型进行浅拷贝实际上是对引用的一个拷贝，两个变量指定的是一个内存地址

my_tuple1 = (3, 5)
my_tuple2 = copy.copy(my_tuple1)
print("my_tuple1:", id(my_tuple1), "my_tuple2:", id(my_tuple2))

# 得知结论: 浅拷贝不会对不可变类型进行拷贝，也就说不会开辟内存内存空间，
# 对于不可变类型进行浅拷贝实际上是对引用的一个拷贝，两个变量指定的是一个内存地址

# 可变类型: 列表、字典、集合
my_list1 = [1, 3, [4, 6]]

my_list2 = copy.copy(my_list1)

print("my_list1:", id(my_list1), "my_list2:", id(my_list2))

my_list1.append(5)
print(my_list1, my_list2)

print("my_list1[2]:", id(my_list1[2]), "my_list2[2]:", id(my_list2[2]))
my_list1[2].append(3)
print(my_list1, my_list2)