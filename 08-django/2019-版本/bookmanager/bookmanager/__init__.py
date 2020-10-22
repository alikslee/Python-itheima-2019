import pymysql

# 让Django的ORM能以mysqldb的方式来调用PyMySQL
pymysql.version_info = (2, 0, 1, "final", 0)
pymysql.install_as_MySQLdb()
