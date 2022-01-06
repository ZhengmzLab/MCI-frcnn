echo "traing data name"
read OUT
touch $OUT.ANNO.txt
for F in *.json
do
python SH02_json2annotxt.py $F $OUT
PICANNO=$(ls $F|rev|cut -d"." -f2-|rev)".png.ANNO.txt"
cat $PICANNO >> $OUT.ANNO.txt
done
cat $OUT.ANNO.txt
