2023/11/14
import os
from os.path import join, getsize
for root, dirs, files in os.walk("C:\\xhs\\"):
        print(root, "占用", end="")
        print(sum(getsize(join(root, name)) for name in files), end="")
        print("bytes in", len(files), "文件数量")
        if 'test' in dirs:
            print("test")
"""
os.walk("C:\\xhs\\")返回一个生成器，可以递归迭代一个文件夹
每迭代一次返回所在路径，文件夹名，文件名，
直到所有文件夹被迭代一遍后这个生成器迭代完毕，部分源代码如下
    # Yield before recursion if going top down
    if topdown:
        yield top, dirs, nondirs

        # Recurse into sub-directories
        islink, join = path.islink, path.join
        for dirname in dirs:
            new_path = join(top, dirname)
            # Issue #23605: os.path.islink() is used instead of caching
            # entry.is_symlink() result during the loop on os.scandir() because
            # the caller can replace the directory entry during the "yield"
            # above.
            if followlinks or not islink(new_path):
                yield from _walk(new_path, topdown, onerror, followlinks)
    else:
        # Recurse into sub-directories
        for new_path in walk_dirs:
            yield from _walk(new_path, topdown, onerror, followlinks)
        # Yield after recursion if going bottom up
        yield top, dirs, nondirs
"""