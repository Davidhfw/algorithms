# 编写一个函数, 给定一个目录,返回这个目录下的所有文件

import os

def traversal_files(parent_path):
    if not os.path.exists(parent_path):
        return
    dirs = os.listdir(parent_path)
    # print(dirs)
    res_files = []
    for file in dirs:
        file_path = os.path.join(parent_path, file)
        # 判断是否为文件
        if os.path.isfile(file_path):
            # res_files.append(file)
            print(file_path)
        else:
            traversal_files(file_path)
    # return res_files


parent_path = os.getcwd()
res = traversal_files(parent_path)
print(res)
