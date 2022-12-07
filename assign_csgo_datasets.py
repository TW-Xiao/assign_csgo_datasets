import os
import random
import shutil
from glob import glob

"""
以下操作只针对csgo-jpg-6000
只需修改以下参数即可完成数据集的划分:
val_num 所需验证集的数量
src_dir_labels 标签原本存放的文件地址
dst_dir_labels 标签移动的目标文件地址
src_dir_images 图片移动的存放文件地址
dst_dir_images 图片移动的目标文件地址
"""


def mymovefile(srcfile, dstpath):  # 移动文件的函数
    if not os.path.isfile(srcfile):
        print("%s not exist!" % (srcfile))
    else:
        fpath, fname = os.path.split(srcfile)  # 分离文件名和路径
        if not os.path.exists(dstpath):
            os.makedirs(dstpath)  # 创建路径
        shutil.move(srcfile, dstpath + fname)  # 移动文件
        print("move %s -> %s" % (srcfile, dstpath + fname))


val_num = 1385  # 先人工算出你要划分的验证集的数量
labels_filepath = '/home/xiaotaowen/csgo-jpg-6000/labels'  # 加载验存放证集txt文件的路径
total_labels = os.listdir(labels_filepath)
num = len(total_labels)  # 统计数据集txt文件的数量
list_images = range(num)  # 创建一个长度为num的列表
val_labels_num = int(num * val_percent)  # 验证集的数量为数据集总数的20%
val = random.sample(list_images, val_percent)  # 在数据集中随机取val_num张图片作为验证集

for i in val:
    src_dir_labels = os.path.join('/home/xiaotaowen/csgo-jpg-6000/labels/', str(i).zfill(6) + ".txt")
    dst_dir_labels = '/home/xiaotaowen/csgo-jpg-6000/labels_train_val/val/'
    src_dir_images = os.path.join('/home/xiaotaowen/csgo-jpg-6000/images/', str(i).zfill(6) + ".jpg")
    dst_dir_images = '/home/xiaotaowen/csgo-jpg-6000/images_train_val/val/'
    mymovefile(src_dir_labels, dst_dir_labels)  # 移动文件
    mymovefile(src_dir_images, dst_dir_images)  # 移动文件



