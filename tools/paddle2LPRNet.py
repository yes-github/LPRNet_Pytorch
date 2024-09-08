# -*- coding: utf-8 -*-
import os
import shutil


# 将paddle标注的车牌图片数据转成LPRNet格式（图片名即为车牌内容）
if __name__ == "__main__":
    with open("Z:/train_data/rec/train.txt", 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for line in lines:
        columns = line.strip().split('\t')
        src_file_path = columns[0]
        dest_file_name = columns[1]
        dest_file_path = os.path.join("z:/LPRNet_Data", "%s.jpg" % dest_file_name)

        shutil.copy2(src_file_path, dest_file_path)


        