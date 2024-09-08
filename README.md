# LPRNet_Pytorch
Pytorch Implementation For LPRNet, A High Performance And Lightweight License Plate Recognition Framework.  
完全适用于中国车牌识别（Chinese License Plate Recognition）及国外车牌识别！  
目前仅支持同时识别蓝牌和绿牌即新能源车牌等中国车牌，但可通过扩展训练数据或微调支持其他类型车牌及提高识别准确率！

# dependencies

- pytorch >= 1.0.0
- opencv-python 3.x
- python 3.x
- imutils
- Pillow
- numpy

# pretrained model

* [pretrained_model](https://github.com/sirius-ai/LPRNet_Pytorch/tree/master/weights/)

# training and testing

1. prepare your datasets, image size must be 94x24.
2. base on your datsets path modify the scripts its hyperparameters --train_img_dirs or --test_img_dirs.
3. adjust other hyperparameters if need.
4. run 'python train_LPRNet.py' or 'python test_LPRNet.py'.
5. if want to show testing result, add '--show true' or '--show 1' to run command.

# performance

- personal test datasets.
- include blue/green license plate.
- images are very widely.
- total test images number is 27320.

|  size  | personal test imgs(%) | inference@gtx 1060(ms) |
| ------ | --------------------- | ---------------------- |
|  1.7M  |         96.0+         |          0.5-          |

# References

1. [LPRNet: License Plate Recognition via Deep Neural Networks](https://arxiv.org/abs/1806.10447v1)
2. [PyTorch中文文档](https://pytorch-cn.readthedocs.io/zh/latest/)

# 常见问题
- [AttributeError: module 'torch.utils.data' has no attribute 'collate'](https://blog.csdn.net/weixin_45354497/article/details/129755744)
    - 解决办法：将`D:\bin\Anaconda3\lib\site-packages\torch\utils\data\_utils\collate.py`文件复制到上一级目录`D:\bin\Anaconda3\lib\site-packages\torch\utils\data\collate.py`即可
- [cv2.destroyAllWindows() => cv2.error: OpenCV(4.10.0) D:\a\opencv-python\opencv-python\opencv\modules\highgui\src\window.cpp:1295: error: (-2:Unspecified error) The function is not implemented. Rebuild the library with Windows, GTK+ 2.x or Cocoa support. If you are on Ubuntu or Debian, install libgtk2.0-dev and pkg-config, then re-run cmake or configure script in function 'cvDestroyAllWindows'](https://blog.csdn.net/tsyccnh/article/details/102915803)
    - 解决办法：重新安装`opencv-contrib-python`
    ```bash
    pip uninstall opencv-contrib-python
    pip install opencv-contrib-python
    ```