# schoolcard_detection
ntu schoolcard detection

## About The Project

![1587557301042](https://wx3.sinaimg.cn/mw690/006ocjslgy1ge2sxh7numj30ji0fc7sh.jpg)

检测图片中的NTU校园卡

## How to train

You can see function "get_dataset" in the file "train_yolo.py" to set dataset path. An example, download dataset and unzip to the path such as "D:\VOCdevkit\VOC2028", train/val dataset can set as:

```
train_dataset = VOCLike(root='D:\VOCdevkit', splits=[(2028, 'trainval')])
val_dataset = VOCLike(root='D:\VOCdevkit', splits=[(2028, 'test')])
```

Then check train_yolo.py to set options and train, such as:

```
python train_yolo.py --batch-size 4 -j 4 --warmup-epochs 3
```

## Getting Started

![1587557558546](https://wx3.sinaimg.cn/mw690/006ocjslgy1ge2t1im6mbj30im02l0sn.jpg)

Modify the parameter file path and picture path to your own parameters and pictures，and then

```
python demo_yolo.py
```

## Concact

[1351161572@qq.com](mailto:1351161572@qq.com)