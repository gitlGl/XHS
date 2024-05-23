"""
SSH的全称是Secure Shell，它是一种网络协议，用于在不安全的网络中安全地进行远程访问和执行命令。
SSH通过加密方式对网络连接进行保护，防止信息被窃听、篡改或伪造。
SSH协议最初由Tatu Ylönen在1995年开发，成为保护远程连接安全的标准解决方案之一。
"""

"""
以下为生成 SSH 密钥的简单命令：
ssh-keygen -t rsa -C "youremail@example.com" 和 ssh-keygen -t rsa -b 2048 -f /path/to/new_key 
-t 表示密钥类型，可以是 rsa、dsa、ecdsa 等。-b 表示密钥长度，默认为2048。
-C 参数用于设置注释信息，这个注释位于公钥末尾。 -f 参数用于指定密钥路径以及文件名。
"""

"""
当你使用 SSH 登录时，默认情况下会从用户的C:\Users\Administrator\.ssh（默认路径）下获取私钥进行解密。
SSH 客户端会在登录时自动查找该路径下的私钥文件，并将其用于解密身份验证所需的信息。
除了填写公钥验证以外，还可以通过账户与密码进行验证。

比如git仓库关联github远程仓库后，提交代码需要验证公钥，
大致流程是流程是github会加密一段“内容”发送给git，（实际流程更复杂）
git会从C:\Users\Administrator\.ssh获取私钥解密这段内容重新发送给github，
如果“内容”相同则验证通过，开始进行加密通信
注意：C:\Users\Administrator\.ssh中可能有多个密钥对，SSH 客户端会依次尝试这些路径下的私钥文件，
直到找到合适的私钥进行身份验证。

平时使用得比较多的SSH客户端是PuTTY和Xshell，Xftp

比较著名的有python第三方库paramiko用于在SSH协议上执行命令和文件传输操作。

Fabric：Fabric是一个用于自动化部署和系统管理的Python库，
它建立在Paramiko之上，并提供了更高级的接口和功能

Spur：Spur是一个轻量级的Python库，基于Paramiko和Shell库，
用于执行远程命令。它提供了简洁的API来连接到远程主机，并执行命令、获取输出等操作。



"""
#ssh链接命令
#ssh lin@172.31.128.118

   