# MCI-frcnn

***

Simon Zhongyuan Tian, Pengfei Yin, Kai Jing, Yang Yang, Yewen Xu, Guangyu Huang, Duo Ning, Melissa J. Fullwood, and Meizhen Zheng. 2022. “MCI-Frcnn: A Deep Learning Method for Topological Micro-Domain Boundary Detection.” Frontiers in Cell and Developmental Biology 10 (November): 1050769. https://doi.org/10.3389/fcell.2022.1050769.


* MC-frcnn is a deep learning based object detector used for micro-domain boundary detection.
* MCI-frcnn derived Faster R-CNN with modifications from  [https://github.com/kbardool/keras-frcnn](https://github.com/kbardool/keras-frcnn).


## Enviroment
```
Ubuntu==16.06
python==3.6.13
tensorflow==2.2.0
keras==2.3.1
opencv==3.4.2
h5py==2.10.0
```


## 1. Using (LabelMe) to draw ground truth boundary of micro-domains
```
SH00.rename.image.and.json.sh
SH02.run.json2anno.sh
```

## 2. Training RPN with script:
```
SH10.run.training.sh
```
## 3. Detecting micro-domain using script:
```
SH11.run.detecting.sh
```
## 4. Formating micro-domain coordinates
```
SH12.sta.sh
SH13_FILTER_ANNO.py
SH15_COOR_PIC_CONNECT.py
SH30.adjustanno.sh
```

## 5. Mesuare traing quality
```
SH32.run.measure.sh
```
