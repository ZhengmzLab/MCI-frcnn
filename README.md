# MCI-frcnn

* * *

MCI-frcnn derived Faster R-CNN with modifications from  [https://github.com/kbardool/keras-frcnn](https://github.com/kbardool/keras-frcnn).


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
>SH11.run.detecting.sh

## 4. Formating micro-domain coordinates
```
```

## 5. Mesuare traing quality
```
SH32.run.measure.sh
```
