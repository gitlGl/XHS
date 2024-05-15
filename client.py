import socket
import ssl,time

def establish_secure_connection(host, port, ca_cert_file):
   
    # 创建一个 SSL 上下文
    context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
    context.load_verify_locations(ca_cert_file)

    # 设置验证模式为必需
    context.verify_mode = ssl.CERT_REQUIRED

    # 设置不检查主机名
    context.check_hostname = False


    sock = socket.create_connection((host, port)) 
    #包装程触发ssl握手验证
    #其中包括服务器发送其证书给客户端，然后客户端验证服务器的证书。
    #简单情况下就可以互相交换公钥进行加密通信
    with context.wrap_socket(sock, server_hostname=host) as ssock:
        cert = ssock.getpeercert()
        print(cert.items())#打印出服务器的证书信息
        
        while True:
            ssock.send(b"Hello, server!")
            data = ssock.recv(1024)
            print(data.decode())
            time.sleep(2)
                
host = "localhost"
port = 8443

#使用根证书文件进行验证
ca_cert_file = "cert/ca-cert.pem"  
establish_secure_connection(host, port, ca_cert_file)



