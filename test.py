#2023/12/13
"""
book = load_workbook("词频统计.xlsx")
book.save("词频统计.xlsx")

用openyxl操作excel文件运行期间退出终端（强制退出进程）会
导致文件损坏，经过测试是上面两行代码没执行完便强制退出导致，
想起来pyqt里面关闭窗口便会执行eventclse函数，但是关闭窗口其实是
属于键盘/鼠标中断信号，跳转中断函数处理资源后主动退出，
与关闭终端强被制退出不是一个概念，关闭终端后，终端中的子进程会被kill掉，
当然也可以通过参数独立运行进程，使得不受终端影响。关机时候偶尔提醒有程序未退出，
是避免关机关闭进程后导致应用程序文件损坏，现在程序越来越规范比较少出现提示程序未退出，
因为关机时候会发送关机信号给应用程序，应用程序也相应的设计了接收关机信号后的处理函数。
"""
import signal
flag = 0#中断退出标志
def signal_handler(sig, frame):
    while True:
        f = input("退出程序？输入Y/N:")
        if f == "Y" or f == 'y':
            global flag
            flag = 1
            break
        if f == "N" or f == 'n':
            break
    
    #print(sig,type(sig))#(type int)
    # frame为调用函数堆栈
    # stack = traceback.extract_stack(frame)
    # for file_name, lineno, function, _ in stack:
    #     print(file_name,lineno,function)
    # locals_dict = frame.f_locals
    # # for var_name, var_value in locals_dict.items():
    # #     print(f"{var_name} = {var_value}")