from contextlib import contextmanager


# 加上装饰器这个代码，那么下面函数创建的对象就是一个上下文管理器
@contextmanager
def my_open(file_name, file_mode):

    try:
        file = open(file_name, file_mode)
        # yield关键之前的代码可以认为是上文方法，负责返回操作对象资源
        yield file
    except Exception as e:
        print(e)
    finally:
        print("over")
        # yield关键字后面的代码可以任务是下文方法，负责释放操作对象的资源
        file.close()


# 普通函数不能结合with语句使用，with语句结合上下文管理器
with my_open("1.txt", "r") as file:
    # file_data = file.read()
    # print(file_data)
    file.write('sss')