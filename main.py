# -*- coding: UTF-8 -*-
import os
sourse_file = [[],[],[]] #储存需要备份的文件内容
back_file =[[],[],[]]    #储存已备份文件夹中的内容
copy_file =[[],[],[]]
print ('hello world')
path = 'C:\\Users\\Link\\Desktop'


def readFileList(myList,path):
    """
        读取文件列表，并且创造一个三维列表，内涵目录下所有文件名字
        Args:
            myList:储存信息的三维数组
            path:需要读取的目录
    """
    for root,dir,file in os.walk(path):
        print(file)
readFileList(sourse_file,path)