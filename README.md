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

# 部署依赖
```bash
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
pip3 install imutils
```

# 中国车牌数据
### [CCPD](https://github.com/detectRecog/CCPD)
- [2021黄牌](https://aistudio.baidu.com/datasetdetail/101671)
- [2020绿牌](https://aistudio.baidu.com/datasetdetail/101595)
- [2019蓝牌](https://aistudio.baidu.com/datasetdetail/101613)

# 从训练数据中抽取文件作为测试数据
```bash
find . -type f -name 'Z*.jpg' | tail -n 1 | xargs -I {} mv {} /home/ye/CODE/MY/LPRNet_Pytorch/data/test/Brazil
```

# 常见问题
- [AttributeError: module 'numpy' has no attribute 'int'.](https://blog.csdn.net/weixin_46669612/article/details/129624331)
    - 解决办法：将numpy的方法np.int改为np.int_
- [AttributeError: module 'torch.utils.data' has no attribute 'collate'](https://blog.csdn.net/weixin_45354497/article/details/129755744)
    - 解决办法：将`D:\bin\Anaconda3\lib\site-packages\torch\utils\data\_utils\collate.py`文件复制到上一级目录`D:\bin\Anaconda3\lib\site-packages\torch\utils\data\collate.py`即可
- [cv2.destroyAllWindows() => cv2.error: OpenCV(4.10.0) D:\a\opencv-python\opencv-python\opencv\modules\highgui\src\window.cpp:1295: error: (-2:Unspecified error) The function is not implemented. Rebuild the library with Windows, GTK+ 2.x or Cocoa support. If you are on Ubuntu or Debian, install libgtk2.0-dev and pkg-config, then re-run cmake or configure script in function 'cvDestroyAllWindows'](https://blog.csdn.net/tsyccnh/article/details/102915803)
    - 解决办法：重新安装`opencv-contrib-python`
    ```bash
    pip uninstall opencv-contrib-python
    pip install opencv-contrib-python
    ```
- [ValueError: setting an array element with a sequence. The requested array has an inhomogeneous shape after 1 dimensions. The detected shape was (100,) + inhomogeneous part.](https://blog.csdn.net/qwerpoiu66/article/details/130902870)
    - 解决办法：
    ```
    pip uninstall numpy
    pip install numpy==1.22.3
    ```