import socket


if __name__ == '__main__':

    # 1. 创建tcp客户端套接字
    # AF_INET: ipv4地址类型
    # SOCK_STREAM： tcp传输协议类型
    tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 提示: 客户端程序不强制要求绑定端口号
    tcp_client_socket.bind(("", 8900))
    # 2. 和服务端套接字建立连接
    tcp_client_socket.connect(("192.168.22.78", 9090))

    send_content = "你好,我是客户端小白!!" # input()
    # 对字符串进程编码成为二进制数据
    send_data = send_content.encode("utf-8")

    # 3. 发送数据到服务端
    # windows里面的网络调试助手使用的gbk编码
    # linux 里面的络调试助手使用的utf-8编码
    tcp_client_socket.send(send_data)
    # 4. 接收服务端的数据
    # 1024：表示每次接收的最大字节数
    recv_data = tcp_client_socket.recv(1024)
    # 对二进制数据进行解码
    recv_content = recv_data.decode("utf-8")
    print("接收服务端的数据为:", recv_content)
    # 5. 关闭套接字
    tcp_client_socket.close()
