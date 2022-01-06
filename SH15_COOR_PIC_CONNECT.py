"""
(tf1) simon@ubuntu:/mnt/hgfs/DEEP/FRCNN.2021OCT03/results_imgs.TEST.5PIC.DEMO$ cat RAID_5PIC
chr2L	71365	306985	RAID_R5	5000001	956000002
chr2L	345339	574906	RAID_R5	5000002	956000004
chr2L	811239	872685	RAID_R5	5000003	956000006
chr2L	1060031	1191164	RAID_R5	5000004	956000008
chr2L	1360909	1476309	RAID_R5	5000005	956000010
(tf1) simon@ubuntu:/mnt/hgfs/DEEP/FRCNN.2021OCT03/results_imgs.TEST.5PIC.DEMO$ cat DETAIL.txt
R001.png,352,80,704,176,a	R001.png,1136,416,96.82028293609619
R001.png,640,0,880,80,a	R001.png,1136,416,98.50292801856995
R001.png,144,224,416,320,a	R001.png,1136,416,99.39191341400146
R001.png,32,208,496,336,a	R001.png,1136,416,82.23366141319275
R001.png,944,176,1136,224,a	R001.png,1136,416,97.20003604888916
R001.png,416,96,528,176,a	R001.png,1136,416,98.74568581581116
R002.png,848,112,1104,304,a	R002.png,1136,416,92.38229393959045
R002.png,80,112,512,272,a	R002.png,1136,416,85.83942651748657

"""
R="SBM56_RAID5_RGAP6.stdbin.stp.CMB.UID.RAID_ONLY"
D={}
FR=open(R,"r")
while True:
    line=FR.readline()
    if not line:
        break
    word=line.rstrip("\n").split("\t")
    C=word[0]
    S=word[1]
    E=word[2]
    NAME=word[4]
    NEWNAME="R"+str(NAME[4:])
    D[NEWNAME]={"S":S,"E":E,"C":C}
#print(D)
IN="DETAIL.txt"
FIN=open(IN,"r")
FOUT=open("MTF.txt","w")
while True:
    line=FIN.readline()
    if not line:
        break
    word=line.rstrip("\n").split("\t")
    pic_name=word[0].split(".")[0]
    pic_left_boarder=0
    pic_right_boarder=int(word[1].split(",")[1])
    pic_region_left_x=int(word[0].split(",")[1])
    pic_region_right_x=int(word[0].split(",")[3])
    raid_name=pic_name
    gnm_left_boarder=int(D[raid_name]["S"])
    gnm_right_boarder=int(D[raid_name]["E"])
    ratio=(gnm_right_boarder-gnm_left_boarder)/(pic_right_boarder-pic_left_boarder)
    gnm_region_left_x=int(ratio*pic_region_left_x)
    gnm_region_right_x=int(ratio*pic_region_right_x)
    #print(gnm_region_left_x,gnm_region_right_x)
    RAIDLINE=",".join(["RAID",raid_name,D[raid_name]["C"],str(gnm_left_boarder),str(gnm_right_boarder)])
    MTFLINE=",".join(["MTF",raid_name,D[raid_name]["C"],str(gnm_region_left_x),str(gnm_region_right_x)])
    newline="\t".join([word[0],MTFLINE,word[1],RAIDLINE])
    FOUT.write(newline+"\n")
