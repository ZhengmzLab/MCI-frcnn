import json
import operator
import collections
import os,sys
from datetime import datetime
TIMELINE=datetime.now().strftime("%Y%d%m%H%M%S")

#FILE='Picture1.json'
FILE=sys.argv[1]

OUTNAME=sys.argv[2]
f=open(FILE,'r')
data = json.load(f)
PICNAME=FILE.split(".")[0]+".png"
DOUT=OUTNAME+".PICDIR"
FANNO=PICNAME+".ANNO.txt"
OUTANNO=OUTNAME+".ANNO.txt"
FOUT=open(FANNO,"w")

os.system("mkdir "+DOUT)
for SP in data['shapes']:
 CLASSNAME=SP['label']   
 #print(SP['points'])
 DX={}
 DY={}
# print(len(SP['points']))
 PTS=SP['points']
 for i in range(len(PTS)):
  x=PTS[i][0]
  y=PTS[i][1] 
  DX[i+1000]=x
  DY[i+1000]=y
 sorted_value_x=sorted(DX.values())
 SDX={}
 for j in sorted_value_x:
  for k in DX.keys():
   if DX[k] == j:
    SDX[k]=DX[k]
 print(SDX)
 A=list(SDX)[0]
 B=list(SDX)[1]
 C=list(SDX)[2]
 D=list(SDX)[3]
 VAX=SDX[A]
 VBX=SDX[B]
 VCX=SDX[C]
 VDX=SDX[D]
 print(A,B,C,D)
 print(VAX,VBX,VCX,VDX)
 VAY=DY[A]
 VBY=DY[B]
 VCY=DY[C]
 VDY=DY[D]
 print(VAY,VBY,VCY,VDY)
 if VAY <= VBY:
  LBKEY=A
  LBX=VAX
  LBY=VAY
 else:
  LBKEY=B
  LBX=VBX
  LBY=VBY
 if VDY >= VCY:
  RTKEY=D
  RTX=VDX
  RTY=VDY
 else:
  RTKEY=C
  RTX=VCX
  RTY=VCY
 print(LBKEY,LBX,LBY)
 print(RTKEY,RTX,RTY)
 print(CLASSNAME,PICNAME)
 FPTH=DOUT+"/"+PICNAME
 newline=",".join([FPTH,str(int(LBX)),str(int(LBY)),str(int(RTX)),str(int(RTY)),CLASSNAME])
 FOUT.write(newline+"\n")
f.close()
os.system("cp "+PICNAME+"  "+DOUT)
