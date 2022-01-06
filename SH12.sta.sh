echo "input test flder:"
read TEST
cd $TEST
cp ../SH15_COOR_PIC_CONNECT.py .
cp ../SH13_FILTER_ANNO.py .
cp ../SBM56_RAID5_RGAP6.stdbin.stp.CMB.UID.RAID_ONLY . 
python SH13_FILTER_ANNO.py
wait
python SH15_COOR_PIC_CONNECT.py


cd ../
