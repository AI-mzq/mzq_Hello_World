# -*- coding:utf8 -*-
'''
批量重命名文件夹中的图片文件
我依次把三个文件夹的更新了一下，抽查的几个，发现按照统一规则转换的是对应着的
'''
# !/usr/bin/python3
import os


class BatchRename():

    def __init__(self):
        self.path1 = r'/data/sdxx/mzq/YOLOv3/YOLOv3-New-fire/YOLOv3-SaveVideo-New/dataset/all_data/new_fire_dataset/labels/'  # 我把txt和image都改了下路径
       #  self.path2 = r'F:/fire_data/SSD_fire_data/firename/'

    def rename(self):
        filelist = os.listdir(self.path1)
        print(filelist)
        total_num = len(filelist)
        i = 20001
        #
        for item in filelist:
            if item.endswith('.txt'):
                src = os.path.join(os.path.abspath(self.path1), item)
                str1 = str(i)
                dst = os.path.join(os.path.abspath(self.path1), str1.zfill(6) + '.txt') #str1.zfill(x),x为一共几位数，用0补齐，如001000
                # print(dst)
                try:
                    os.rename(src, dst)
                    print('converting %s to %s ...' % (src, dst))
                    i = i + 1
                except:
                    continue
        # print
        # 'total %d to rename & converted %d jpgs' % (total_num, i)


if __name__ == '__main__':
    demo = BatchRename()
    demo.rename()
