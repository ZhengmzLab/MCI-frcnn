#training.2021OCT20.201PIC.ANNO.txt
echo "echo training annotation file"
echo "e.g. training.2021OCT20.201PIC.ANNO.txt"
read F
nohup python SH10_train_frcnn_simon.py -o simple -p $F  > $F.log 2>&1 &  ###MTF.TRAING.50PIC.ANNO.txt



