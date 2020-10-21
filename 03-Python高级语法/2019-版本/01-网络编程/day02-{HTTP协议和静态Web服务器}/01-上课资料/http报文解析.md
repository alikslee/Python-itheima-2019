
----http get请求报文
----请求行-----
GET / HTTP/1.1 => 请求方法(方式) 请求的资源路径 http协议的版本
----请求头----
Host: www.itcast.cn  => 服务器的主机ip地址和端口号，提示如果看不到端口号默认是80
Connection: keep-alive => 和服务端程序保存长连接，当客户端和服务端有一段时间(3-5)没有进行通信，那么服务器程序会主动向客户端断开连接
Upgrade-Insecure-Requests: 1 => 让客户端请求不安全请求，以后要使用https
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36 => 用户代理，客户端程序名称，当后续讲爬虫的时候可以根据是否有User-Agent进行反爬机制
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3 => 告诉服务端程序可以接受的数据类型
Accept-Encoding: gzip, deflate => 告诉服务端程序支持的压缩算法
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8 => 告诉服务端程序支持的语言
Cookie: UM_distinctid=169f06ab9d21a-0a52d93224ce3-12376d57-13c680-169f06ab9d571a; accessId=22bdcd10-6250-11e8-917f-9fb8db4dc43c; bad_id22bdcd10-6250-11e8-917f-9fb8db4dc43c=5c8a5a11-5811-11e9-975d-5932d6370ce7; parent_qimo_sid_22bdcd10-6250-11e8-917f-9fb8db4dc43c=69928890-5811-11e9-ac5b-eb2506ccad9a; CNZZDATA4617777=cnzz_eid%3D324231225-1554516145-%26ntime%3D1554521548; href=http%3A%2F%2Fwww.itcast.cn%2F; pageViewNum=5; Hm_lvt_0cb375a2e834821b74efffa6c71ee607=1554516722,1554523431; Hm_lpvt_0cb375a2e834821b74efffa6c71ee607=1554523431; nice_id22bdcd10-6250-11e8-917f-9fb8db4dc43c=fc5f90f1-5820-11e9-b896-dba72e2578c0; openChat22bdcd10-6250-11e8-917f-9fb8db4dc43c=true => 客户端用户身份的标识
-----空行-----
\r\n

-----http get请求的原始报文数据------------

----请求行-----
GET / HTTP/1.1\r\n
----请求头----
Host: www.itcast.cn\r\n
Connection: keep-alive\r\n
Upgrade-Insecure-Requests: 1\r\n
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36\r\n
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3\r\n
Accept-Encoding: gzip, deflate\r\n
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8\r\n
Cookie: UM_distinctid=169f06ab9d21a-0a52d93224ce3-12376d57-13c680-169f06ab9d571a; accessId=22bdcd10-6250-11e8-917f-9fb8db4dc43c; bad_id22bdcd10-6250-11e8-917f-9fb8db4dc43c=5c8a5a11-5811-11e9-975d-5932d6370ce7; parent_qimo_sid_22bdcd10-6250-11e8-917f-9fb8db4dc43c=69928890-5811-11e9-ac5b-eb2506ccad9a; CNZZDATA4617777=cnzz_eid%3D324231225-1554516145-%26ntime%3D1554521548; href=http%3A%2F%2Fwww.itcast.cn%2F; pageViewNum=5; Hm_lvt_0cb375a2e834821b74efffa6c71ee607=1554516722,1554523431; Hm_lpvt_0cb375a2e834821b74efffa6c71ee607=1554523431; nice_id22bdcd10-6250-11e8-917f-9fb8db4dc43c=fc5f90f1-5820-11e9-b896-dba72e2578c0; openChat22bdcd10-6250-11e8-917f-9fb8db4dc43c=true\r\n
-----空行-----
\r\n

-----http get请求报文的格式----
请求行\r\n
请求头\r\n
空行(\r\n)

提示: 每项信息之间都需要一个\r\n，是要http协议规定

-----http post请求报文的格式----
请求行\r\n
请求头\r\n
空行(\r\n)
请求体

提示: 请求体就是浏览器发送给服务器的数据

----http 响应报文解析----
---- 响应行(状态行) --------
HTTP/1.1 200 OK => http协议版本 状态码 状态描述
---- 响应头 ----------
Server: Tengine => 服务器的名称
Content-Type: text/html; charset=UTF-8  => 服务器发送给浏览器的内容类型及编码格式
Transfer-Encoding: chunked => 服务器发送给客户端程序(浏览器)的数据不确定数据长度， 数据发送结束的接收标识: 0\r\n，Content-Length: 200（字节），服务器发送给客户端程序的数据确定长度。 内容长度这两个选项只能二选一
Connection: keep-alive  => 和客户端保持长连接
Date: Sat, 06 Apr 2019 08:49:57 GMT => 服务器的时间
--- 以下都是自定义响应头信息，字节定义响应头的名字和响应头的值，比如: is_login: True
Accept-Ranges: bytes
Ali-Swift-Global-Savetime: 1554540597
Via: cache45.l2nu29-1[3,200-0,M], cache11.l2nu29-1[4,0], kunlun2.cn249[30,200-0,M], kunlun2.cn249[33,0]
X-Cache: MISS TCP_MISS dirn:-2:-2
X-Swift-SaveTime: Sat, 06 Apr 2019 08:49:57 GMT
X-Swift-CacheTime: 0
Timing-Allow-Origin: *
EagleId: 2a51041615545405973986157e
----- 空行 ----
\r\n
----- 响应体 就是真正意义上给浏览器解析使用的数据----
网页数据


提示： 对于请求头和响应头信息程序员都可以进行自定义，按照客户端和服务器约定好的方式来制定即可。

----http 响应原始报文解析----
---- 响应行(状态行) --------
HTTP/1.1 200 OK\r\n
---- 响应头 ----------
Server: Tengine\r\n
Content-Type: text/html; charset=UTF-8\r\n
Transfer-Encoding: chunked\r\n
Connection: keep-alive\r\n
Date: Sat, 06 Apr 2019 08:49:57 GMT\r\n
--- 以下都是自定义响应头信息，字节定义响应头的名字和响应头的值，比如: is_login: True
Accept-Ranges: bytes\r\n
Ali-Swift-Global-Savetime: 1554540597\r\n
Via: cache45.l2nu29-1[3,200-0,M], cache11.l2nu29-1[4,0], kunlun2.cn249[30,200-0,M], kunlun2.cn249[33,0]\r\n
X-Cache: MISS TCP_MISS dirn:-2:-2\r\n
X-Swift-SaveTime: Sat, 06 Apr 2019 08:49:57 GMT\r\n
X-Swift-CacheTime: 0\r\n
Timing-Allow-Origin: *\r\n
EagleId: 2a51041615545405973986157e\r\n
----- 空行 ----
\r\n
----- 响应体 就是真正意义上给浏览器解析使用的数据----
网页数据


---- http响应报文的格式 -----

响应行\r\n
响应头\r\n
空行\r\n
响应体\r\n

提示: 每项信息之间都要有一个\r\n进行分割








