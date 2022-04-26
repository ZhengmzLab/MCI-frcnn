# MCI-frcnn

* * *

* MC-frcnn is a deep learning based object detector used for micro-domain boundary detection.
* MCI-frcnn derived Faster R-CNN with modifications from  [https://github.com/kbardool/keras-frcnn](https://github.com/kbardool/keras-frcnn).


##### Enviroment
```
Ubuntu==16.06
python==3.6.13
tensorflow==2.2.0
keras==2.3.1
opencv==3.4.2
h5py==2.10.0
```


## 1. Using Annotation tool (LabelMe) to draw ground truth boundary of micro-domains and reform boundary box infomation
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
