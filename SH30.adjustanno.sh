echo "input RESULT FOLDER"
read RF
#results_imgs.Test.all.476.raid.model_frcnn_0060.hdf5.20212210182252
cat ${RF}/annotation.txt|awk -v NM=$RF '{print NM"/"$0}' > $RF.anno
#cat RESULT.0020/annotation.txt |awk '{print "./RESULT.0020/"$0}' > RESULT.0020.anno

