
ls -d results_imgs.*/

echo "input RESULT FOLDER"
read RF
#results_imgs.Test.all.476.raid.model_frcnn_0060.hdf5.20212210182252
#WT= 0120_0100_0100
#OSError: Unable to open file (unable to open file: name = 'model_frcnn_0120_0100_0120_0100_0100.hdf5', errno = 2, error message = 'No such file or directory', flags = 0, o_flags = 0)

echo "input weight number (model_frcnn_0120_0100_0100.hdf5 ==> WT = 0100 (the last number) )"

read WN
ANNO=${RF}.anno
echo $WN
echo $ANNO
echo $RF
nohup  python SH32_measure_map_simon.py  -o simple -i $WN -p $ANNO  > $RF.meas 2>&1 &
# python LF08.MP3.py  -o simple -i 0060 -p results_imgs.Test.all.476.raid.model_frcnn_0060.hdf5.20212210182252.anno
