To Reader: Sorry, Source code of MCIBox is comming ......
To Reviewer: please access https://github.com/MCIBOX/MCIBox using passcode supplied in Cover letter.
***
# MCI-frcnn


* MC-frcnn is a deep learning based object detector used for micro-domain boundary detection.
* MCI-frcnn derived Faster R-CNN with modifications from  [https://github.com/kbardool/keras-frcnn](https://github.com/kbardool/keras-frcnn).

---
## Enviroment
```
Ubuntu==16.06
python==3.6.13
tensorflow==2.2.0
keras==2.3.1
opencv==3.4.2
h5py==2.10.0
```
---
## Data Preparation Phase

1. Prepare clustered Fragment-view images (*.png*) of micro-domians from single molecule multi-way chromatin interaction data of new-gen 3D genome techniques, such as [ChIA-Drop](http://www.nature.com/articles/s41586-019-0949-1), [SPRITE](https://linkinghub.elsevier.com/retrieve/pii/S0092867418306366) etc.
2. Annotate ground truth bounding box for each micro-domain using [**LabelMe**](https://github.com/wkentaro/labelme) and recordeed in a *.json* file.
3. Create a folder (e.g. *TRAINING_SET/*) as the training set, which includis images(*.png*) and their annotation (*.json*).
4. Format the name of images and annotation files in this way :
```
cd TRAINING_SET/
RNAPII_CHIADROP_RAID_0012.chr8.126000000.126800000.png
RNAPII_CHIADROP_RAID_0012.chr8.126000000.126800000.json
(Image_name_of_a_domain.domian_chrom.domain_start.domian_end.png)
```
5. Generate *.anno* files to feed Faster R-CNN:
```
sh SH01.json2anno.sh

# TRAINING_SET.ANNO.txt
# TRAINING_SET.PICDIR
```

---
## Training Phase

```
sh SH02.training.sh
```
---
## Detecting Phase

```
sh SH03.detecting.sh
```
---
## Measuring Phase

```
sh SH04.measuring.sh
```
---
## Micro-Domain Genomic Coordinates Generation Phase

```
sh SH05.result_get_genomic_coor.sh   # MCI-frcnn detected
sh SH06.labelme_get_genomic_coor.sh  # LabelMe ground truth
```
---
## gIoU Calculating Phase

```
sh SH07.gIoU.sh  
```
---
## Unzip the WEIGHT file

For the size limitation of uploading file to github, we divided out WEIGHT file to two smaller, which can be recovered using this script:

```
SH08.make.weigth.sh
# model_frcnn_3500.hdf5
```

