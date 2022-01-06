"""
ANNO	image_name	R001.png
ANNO	resolution	1136	416
ANNO	R001.png,624,0,864,80,a	100.0
ANNO	R001.png,160,224,384,320,a	100.0
ANNO	R001.png,960,176,1136,224,a	100.0
ANNO	R001.png,416,80,544,176,a	100.0
ANNO	R001.png,416,80,544,176,a	100.0
ANNO	R001.png,160,224,384,320,a	100.0
ANNO	R001.png,416,80,544,176,a	100.0
ANNO	R001.png,416,80,544,176,a	100.0
ANNO	R001.png,160,224,384,320,a	100.0
ANNO	R001.png,160,224,384,320,a	100.0
ANNO	R001.png,624,0,864,80,a	100.0
ANNO	R001.png,432,320,640,352,a	99.99969005584717
ANNO	R001.png,960,176,1136,224,a	100.0
ANNO	R001.png,624,0,864,80,a	100.0
ANNO	R001.png,624,0,864,80,a	100.0
ANNO	R001.png,0,352,192,416,a	99.99998807907104
ANNO	R001.png,960,176,1136,224,a	99.99998807907104
ANNO	R001.png,160,224,384,320,a	100.0
ANNO	R001.png,160,224,384,320,a	100.0
ANNO	R001.png,416,80,544,176,a	100.0
ANNO	R001.png,960,176,1136,224,a	99.99998807907104
ANNO	image_name	R002.png
ANNO	resolution	1136	416
"""
IN="INFO.txt"
FIN=open(IN,"r")
FOUT=open("DETAIL.txt","w")
FILENAME=FIN.readline()
D={}
while True:
 line=FIN.readline()
 if not line:
  break
 if not line.startswith("ANNO"):
  continue
 word=line.rstrip("\n").split("\t")
 if word[1]=="image_name":
  if D != {}:
   pic_name=D["name"]
   pic_width=D["width"]
   pic_height=D["height"]
   for BOX in D:
    if BOX.startswith("R"):
     pos_line=BOX
     score=D[BOX]
     newline1=",".join([pic_name,pic_width,pic_height,score])
     newline=pos_line+"\t"+newline1
     FOUT.write(newline+"\n")
  D={}
  PICNAME=word[2]
  D["name"]=PICNAME
 elif word[1]=="resolution":
  W=word[2]
  H=word[3]
  D["width"]=W
  D["height"]=H
 else:
  box_position=word[1]
  match_score=word[2]
  D[box_position]=match_score

"""
R001.png,416,80,544,176,a	R001.png,1136,416,100.0
R001.png,432,320,640,352,a	R001.png,1136,416,99.99969005584717
R001.png,960,176,1136,224,a	R001.png,1136,416,99.99998807907104
R002.png,0,112,1136,304,c	R002.png,1136,416,99.99983310699463
R002.png,720,0,928,112,a	R002.png,1136,416,100.0
R003.png,0,0,1136,352,b	R003.png,1135,416,99.99082088470459
R004.png,704,0,1120,176,a	R004.png,1130,416,100.0
"""
