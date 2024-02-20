#协程例子
import os
import asyncio,time
async def get_html(n,i):
    # 模拟从网站下载页�?
    print(f"第{n}组第{i}个任�?")
    if n == 2:
        await asyncio.sleep(2)
    else:await asyncio.sleep(1)
    print(f"第{n}组第{i}个任务完�?")

async def task_list(n):
    print(f"第{n}组任务开�?")
    for i in range(1,3):
        asyncio.create_task(get_html(n,i))
    print("安排结束")
    await asyncio.sleep(3)

async def hello():
    print("test")
    await asyncio.sleep(3)

async def hello2():
    print("test2")

async def main():
    # 通过 asyncio.create_task 函数创建任务
    # 调用时需要给它传递一个协程，然后返回一个任务对�?
    lst = []
    for i in range(1,3):
        reuslt =  asyncio.create_task(task_list(i))
        lst.append(reuslt)

    await hello()
    await hello2()
    await asyncio.gather(*lst)
    await asyncio.as_completed(lst)
    
asyncio.run(main(),debug= True)
