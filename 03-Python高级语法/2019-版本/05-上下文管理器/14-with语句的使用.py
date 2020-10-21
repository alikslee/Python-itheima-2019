try:
    file = open("1.txt", "r")
    file.write("abc")
except Exception as e:
    print(e)
finally:
    print('over')
    file.close()


# 为了简化读取文件的操作， python提供了 with 语句的这种写法，既简单又安全，
#  当with语句执行完成，那么关闭文件操作自动完成， 即使有异常以后关闭文件
with open("1.txt", "r") as file:
    # file_data = file.read()
    # print(file_data)
    file.write("sss")

