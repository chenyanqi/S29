import os
# ret = os.path.getsize('D:\Program Files\JetBrains\pythonProject\S29\day08')
# print(ret)

from os.path import join,getsize
def getdirsize(dir):
    size = 0
    for root,dirs,files in os.walk(dir):
        size += sum([getsize(join(root,name)) for name in files])
    return size
if __name__ == '__main__':
    size = getdirsize(r"D:\Program Files\JetBrains\pythonProject\S29")
    print('该目录大小为 %.3f' % (size/1024/1024),'MBi ')
