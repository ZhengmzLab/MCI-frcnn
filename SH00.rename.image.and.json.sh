
cp ../../PURE_RAID_IMG_FROM_TF20201014_LABELME/*.json .
for F in *.json;do NM=$(ls $F|cut -d"." -f1); cp ../../PURE_RAID_IMG_FROM_TF20201014_LABELME/${NM}".png" .;done


