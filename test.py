import multiprocessing

def worker_function(x):
    if x % 2 == 0:  # 模拟偶数输入引发异常
        raise ValueError(f"Error processing {x}")
    return x * 2

def callback(result):
    print(f"Result: {result}")

def err_callback(e):
    print(f"Exception occurred: {e}")


if __name__ == "__main__":
    pool = multiprocessing.Pool(processes=4)

    for i in range(10):
        result = pool.apply_async(worker_function, (i,), 
                        callback=callback,#返回结果回调
                        error_callback=err_callback) # 错误回调

    pool.close()
    pool.join()
import multiprocessing

def worker_function(x):
    if x % 2 == 0:  # 模拟偶数输入引发异常
        raise ValueError(f"Error processing {x}")
    return x * 2

def callback(result):
    print(f"Result: {result}")

def err_callback(e):
    print(f"Exception occurred: {e}")


if __name__ == "__main__":
    pool = multiprocessing.Pool(processes=4)

    for i in range(10):
        result = pool.apply_async(worker_function, (i,), 
                        callback=callback,#返回结果回调
                        error_callback=err_callback) # 错误回调

    pool.close()
    pool.join()
    


import multiprocessing

def work(x):
    if x == 2:
        2 / 0  # 这里会引发异常
    return x * 2

def run(inputs):
    pool = multiprocessing.Pool(processes=4)
    results = []

    for i in inputs:
        result = pool.apply_async(work, (i,))
        results.append(result)
    
    pool.close()
    pool.join()

    for res in results:
        try:
            print(res.get())  # 这里会引发异常
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    run([0, 1, 2, 3])  # 包含一个会引发异常的输入

