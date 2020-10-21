# 1. 函数嵌套
def func_out():
    # 外部函数的变量
    num1 = 10

    def func_inner():
        # 在闭包内修改外部函数的变量
        # num1 = 20  # 本意是修改外部函数变量， 其实是在闭包内定义了一个局部变量
        # 在闭包内修改外部函数的变量需要使用nonlocal关键字
        nonlocal num1
        num1 = 20

        # 2.内部要使用外部函数的变量
        result = num1 + 10
        print(result)

    print("修改前的外部变量:", num1)
    func_inner()
    print("修改后的外部变量:", num1)


    # 3. 返回内部函数
    return func_inner

# 创建闭包对象
new_func = func_out()
new_func()