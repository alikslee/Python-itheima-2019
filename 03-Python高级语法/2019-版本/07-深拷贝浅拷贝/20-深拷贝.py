import copy

# 深拷贝: 只要发现对象有可变类型那么就是对该对象到最后一个可变类型的每一层对象进行拷贝，拷贝成功后会开辟新的内存空间

# 不可变类型： 数字、字符串、元组

num1 = 1
num2 = copy.deepcopy(num1)

print("num1:", id(num1), "num2:", id(num2))

str1 = 'hello'
str2 = copy.deepcopy(str1)

print("str1:", id(str1), "str2:", id(str2))

my_tuple1 = (1, [1,2])
my_tuple2 = copy.deepcopy(my_tuple1)

print("my_tuple1:", id(my_tuple1), "my_tuple2:", id(my_tuple2))
print("my_tuple1[1]:", id(my_tuple1[1]), "my_tuple2[1]:", id(my_tuple2[1]))

my_tuple2[1].append(4)

print(my_tuple1, my_tuple2)

print("my_tuple1[0]:", id(my_tuple1[0]), "my_tuple2[0]:", id(my_tuple2[0]))

# 如果发现元组里面有可变类型那么，会对元组进行拷贝和子元素列表进行拷贝，拷贝后都会产生一个新的内存空间
# 但是不可变类型不会进行拷贝，因为不可变类型不允许在原有内存空间的基础修改数据，
# 所以拷贝没有意义，因为每次修改数据内存地址都会发生变化

# 可变类型： 列表，字典，结合 ， 对应深拷贝来说也会进行拷贝如果发现子对象也是可变类型也会进行拷贝，
# 拷贝后会开辟新的内存空间存储拷贝后的对象

my_list1 = [1,[2, 3]]
my_list2 = copy.deepcopy(my_list1)
print("my_list1:", id(my_list1), "my_list2:", id(my_list2))

print("my_list1[1]:", id(my_list1[1]), "my_list2[1]:", id(my_list2[1]))

# 无论是浅拷贝还是深拷贝都是针对的可变类型