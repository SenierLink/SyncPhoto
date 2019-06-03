# -*- coding: UTF-8 -*-
import os

copy_file =[[],[],[]]
store_file = 'E:'                               #临时文件储存地
old_content_path = store_file + "old.txt"
new_content_path = store_file + "new.txt"
copy_content_path = store_file + "copy.txt"
old_content_file = open(old_content_path, 'w')  #储存需要备份的文件内容
new_content_file = open(new_content_path, 'w')  #储存已备份文件夹中的内容
copy_content_file = open(copy_content_path, 'w')        #储存需要复制的内容

#这两个地址是需要写一个接受键入的
old_path = 'E:\\Honor数据备份'
new_path = 'E:\\Honor数据备份\\Pictures'        


def readFileList(path,filename):
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

old_content_file.close()
new_content_file.close()

for i in new_content:
    if i not in old_content:
        copy_content_file.write(i)      #这里肯定是需要推广的。不然的话一个c盘，一个d盘，就不一样了。这个问题暂时没有想到好的解决办法。
print('完成copy文件的写入')
copy_content_file.close()

copy_content_file = open(copy_content_path, 'w+')        #储存需要复制的内容
copy_content = copy_content_file.readlines()

