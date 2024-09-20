"""//gcc -shared -o test.dll test.c
#include <stdio.h>
#include <windows.h>

__declspec(dllexport) char *test(const char *file_path)
{
    SetConsoleOutputCP(CP_UTF8); // 设置终端输出编码格式为utf8
    //本设备文件系统默认gbk编码，
    //如果python调用的二机制字符串路径是utf8编码，则
    //报错找不到该文件，因为gbk编码的二进制与utf8的二机制不一致
    FILE *file = fopen(file_path, "r");
    if (file == NULL)
    {
        return "无法打开文件";
    }

    char buffer[256];
    while (fgets(buffer, sizeof(buffer), file) != NULL)
    {
        printf("%s", buffer);
    }

    fclose(file); // 关闭文件

    return "测试";
}
"""

import ctypes

# 加载 DLL
lib = ctypes.CDLL(r'C:\Users\Administrator\Desktop\test\test.dll')

# 设置函数参数和返回值类型
lib.test.argtypes = [ctypes.c_char_p]
lib.test.restype = ctypes.c_char_p  # 返回值类型为字符串

# 调用 C 函数，参数为字符串路径的二进制是gbk编码
message = r"C:\Users\Administrator\Desktop\test\测试\test.txt".encode('gbk')
result = lib.test(message)
print(type(result))

# 处理返回值
if result:
    print(result.decode('utf8')) 
    
    
"""
#include <stdio.h>
#include <unistd.h>
//生成dll被python调用
//gcc -shared -o test3.dll test3.c 

__declspec(dllexport) const char* 
get_current_directory(char* buffer, 
size_t size) {
    return getcwd(buffer, size);//获取工作目录
}

    """
    

import ctypes,os

test3 = ctypes.CDLL('./test3.dll')

buffer = ctypes.create_string_buffer(1024)

result = test3.get_current_directory(buffer, ctypes.sizeof(buffer))

try:
    print("Current working directory:", buffer.value.decode('utf8'))
    
except Exception as e:
    print("错误提示：",e)
    print("Current working directory:", buffer.value.decode('gbk'))
    
# 错误提示：'utf-8' codec can't decode byte 0xb2 in position 31: invalid start byte
# Current working directory: C:\Users\Administrator\Desktop\测试中文路径
print(os.getcwd())#python底层会自动处理编码问题
    
    
    
