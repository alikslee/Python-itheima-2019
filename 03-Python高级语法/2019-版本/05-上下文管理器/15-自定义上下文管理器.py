# 上下文管理器: 在类里面实现__enter__ 和 __exit__方法 创建对象就是上下文管理器


# 自定义上下文管理器类
class File(object):
    def __init__(self, file_name, file_mode):
        self.file_name = file_name
        self.file_mode = file_mode

    def __enter__(self):
        # 上文方法，负责返回操作对象资源，比如：文件对象，数据库连接对象
        self.file = open(self.file_name, self.file_mode)
        return self.file

    # 当with语句执行完成以后自动执行__exit__方法
    def __exit__(self, exc_type, exc_val, exc_tb):
        # 下文方法，负责释放对象资源，比如: 关闭文件，关闭数据库连接对象
        print("over")
        self.file.close()

# with 语句结合上下文管理器对象使用
with File("1.txt", "r") as file:
    # file_data = file.read()
    # print(file_data)
    file.write("sss")

