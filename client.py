#
import socket
#创建一个socket，AF_INET指定ipv4协议，如果要用IPv6，就指定为AF_INET6，SOCK_STREAM指定使用面向流的TCP协议
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#建立连接，服务器的IP地址和端口号
s.connect(('www.qq.com.cn',80))
#发送数据，文本格式必须符合http标准
s.send(b'GET / HTTP/1.1\r\nHost: www.qq.com.cn\r\nConnection: close\r\n\r\n')
#接收数据
buffer = []
while True:
#每次最多接收1024个字节
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:#直到recv()返回空数据，表示接收完毕，退出循环
        break
data = d.join(buffer)
#关闭连接，一次完整的网络通信就结束了
s.close()
#接收到的数据包括HTTP头和网页本身，需要把HTTP头和网页分离一下，把HTTP头打印出来，网页内容保存到文件中
header,html = data.split(b'\r\n\r\n',1)
print(header.decode('utf-8'))
#把接收的数据写入文件
with open('qq.html','wb') as f:
    f.write(html)