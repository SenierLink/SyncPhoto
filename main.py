# -*- coding: UTF-8 -*-
import os
sourse_file = [[],[],[]] #储存需要备份的文件内容
back_file =[[],[],[]]    #储存已备份文件夹中的内容
copy_file =[[],[],[]]
store_file = 'E:'
old_content_path = store_file + "old.txt"
new_content_path = store_file + "new.txt"
old_content_file = open(old_content_path, 'a')
new_content_file = open(new_content_path, 'a')
i = 0

print ('hello world')
path = 'E:\\Honor数据备份\\Pictures\\iphone'


def readFileList(myList,path):
    """
        读取文件列表，并且创造一个三维列表，内涵目录下所有文件名字
        Args:
            myList:储存信息的三维数组
            path:需要读取的目录
    """
    for (root,dirs,files) in os.walk(path):
        # old_content_file.wirte(str(files))
        old_content_file.wirte('a')
readFileList(sourse_file,path)