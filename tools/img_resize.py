# -*- coding: utf-8 -*-
import os
import cv2

# 将图片缩放成固定的94*24大小
if __name__ == "__main__":
    directory_path = 'Z:/LPRNet_Data/02'

    # 递归遍历目录
    for root, dirs, files in os.walk(directory_path):
        for filename in files:
            # 检查文件扩展名是否为.jpg
            if filename.lower().endswith('.jpg'):
                # 拼接完整的文件路径
                file_path = os.path.join(root, filename)
                
                img = cv2.imread(file_path)
                new_width = 94
                new_height = 24

                # 缩放图片
                img_resized = cv2.resize(img, (new_width, new_height), interpolation=cv2.INTER_LANCZOS4)
                cv2.imwrite(os.path.join("Z:/LPRNet_Data_94_24/02", filename), img_resized)
                print(f"Found JPG file: {file_path}")