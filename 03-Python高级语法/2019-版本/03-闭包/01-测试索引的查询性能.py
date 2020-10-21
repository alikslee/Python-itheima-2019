import pymysql


if __name__ == '__main__':

    # 创建连接对象
    conn = pymysql.connect(host="localhost",
                    port=3306,
                    user="root",
                    password="mysql",
                    database="python41",
                    charset="utf8")

    # 获取游标，目的是执行sql语句
    cursor = conn.cursor()
    # 准备sql
    sql = "insert into mytest(name) values(%s);"

    try:
        # 循环执行1000次插入数据的操作
        for i in range(10000):
            # 执行sql
            cursor.execute(sql, ["test" + str(i)])

        # 代码执行到此说明添加数据完成，那么提交数据到数据库
        conn.commit()
    except Exception as e:
        # 回滚数据，回到插入之前的一个状态
        conn.rollback()

    finally:
        # 关闭游标
        cursor.close()
        # 关闭连接
        conn.close()