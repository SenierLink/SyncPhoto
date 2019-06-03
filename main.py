# -*- coding: UTF-8 -*-
import os

copy_file =[[],[],[]]
store_file = 'E:'
old_content_path = store_file + "old.txt"
new_content_path = store_file + "new.txt"
copy_content_path = store_file + "copy.txt"
old_content_file = open(old_content_path, 'w')  #储存需要备份的文件内容
new_content_file = open(new_content_path, 'w')  #储存已备份文件夹中的内容
copy_content_file = open(copy_content_path, 'w')        #储存需要复制的内容

old_path = 'E:\\Honor数据备份\\Pictures\\iphone'
new_path = 'E:\\Honor数据备份\\Pictures'


def readFileList(path,filename):
    """
        读取文件列表，并且创造一个三维列表，内涵目录下所有文件名字
        Args:
            myList:储存信息的三维数组
            path:需要读取的目录
    """
    for (root,dirs,files) in os.walk(path):
        for every_root in root:    
            for every_files in files:
                filename.write(str(root)+'\\'+str(every_files)+'\n')      
    print('完成文件写入')
readFileList(old_path,old_content_file)
readFileList(new_path,new_content_file)


old_content_file.close()
new_content_file.close()

old_content_file = open(old_content_path, 'r')  #储存需要备份的文件内容
new_content_file = open(new_content_path, 'r')  #储存已备份文件夹中的内容

old_content = old_content_file.readlines()
new_content = new_content_file.readlines()

print(new_content)
print('========================================================================')
print(old_content)
# for i in new_content
#     if i not in old_content
#         copy_content_file.write(i)
copy_content_file.close()
