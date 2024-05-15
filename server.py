import socket
import ssl,time

def start_secure_server(host, port, server_certfile, server_keyfile):
    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH) 
    #加载证书信任链
    context.load_cert_chain(certfile=server_certfile, keyfile=server_keyfile)
    
    #不验证客户端证书,单向认证
    context.verify_mode = ssl.CERT_NONE
    server_socket = socket.create_server((host, port))
    print(f"Server listening on {host}:{port}...")
    conn, addr = server_socket.accept()
    
    with context.wrap_socket(conn, server_side=True) as ssl_conn:
        print(f"Secure connection established from {addr}")
        handle_client(ssl_conn)

def handle_client(connection):
    while True:
        data = connection.recv(1024)
       
        print(f"Received data from client: {data.decode('utf-8')}")
        connection.send(data.upper())
        time.sleep(2)


host = "localhost"  # 监听本地端口
port = 8443
server_certfile = "cert/server-cert.pem"  # 服务器证书文件路径
server_keyfile = "cert/server-key.pem"  # 服务器私钥文件路径

start_secure_server(host, port, server_certfile, server_keyfile)

"""
生成根证书私钥
openssl genpkey -algorithm RSA -out ca-key.pem
通过私钥生成公钥，私钥可以生成公钥，公钥不可以生成私钥
openssl rsa -in ca-key.pem -pubout -out ca_public_key.pem
 
生成根证书，证书中包含根证书中的公钥
openssl req -new -x509 -key ca-key.pem -out ca-cert.pem -days 3650

创建服务器私钥
openssl genpkey -algorithm RSA -out server-key.pem
通过私钥生成公钥
openssl rsa -in server-key.pem -pubout -out server_public_key.pem

创建服务器证书签名请求
openssl req -new -key server-key.pem -out server-csr.pem

使用根证书对服务器证书进行签名，证书中包含服务器的公钥
openssl x509 -req -in server-csr.pem -CA ca-cert.pem -CAkey ca-key.pem -out server-cert.pem -CAcreateserial -days 3650
    """