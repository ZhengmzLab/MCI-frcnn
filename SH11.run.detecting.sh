ls -d */
echo "input image-dir  TRYING "
read PD
ls model*.hdf5
echo "input WEIGHT model_frcnn_0004.hdf5"
read WT 
python SH11_test_frcnn_simon_6.py -p $PD -w $WT

