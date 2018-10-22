#!/usr/bin/python

# This program is an example to write .xyz file for VESTA
# from the ctrl. file of Questaal lmf code for II-IV-N_2 semiconductors.

# This part, write a .xyz file from ctrl.ext file.

f=open('ctrl.cdsin2','r')
g=open('cdsin2.xyz','w')

g.write('16 \n')
g.write('\n') # only one line space
for line in f:
   if 'ATOM=Cd XPOS=' in line: # N.B the number of spaces is important,here is one space.
      aa=line.split() # N.B. string.split() method
      g.write('Cd  '+aa[2]+' '+aa[3]+' '+aa[4]+'\n')



   if 'ATOM=Si XPOS=' in line:
      aa=line.split() # N.B. string.split() method
      g.write('Si  '+aa[2]+' '+aa[3]+' '+aa[4]+'\n')


   if 'ATOM=N  XPOS=' in line:
      aa=line.split() # N.B. string.split() method
      g.write('N   '+aa[2]+' '+aa[3]+' '+aa[4]+'\n')
f.close()
g.close()
      
# This part is to write .xyz file when "ATOM=  POS "  in ctrl.ext
f=open('ctrl.cdsin2','r')
g=open('cdsin2_pos.xyz','w')

fa=1.000
fb=1.200 # to convert the POS to XPOS
fc=1.100


g.write('16 \n')
g.write('\n') # only one line space
for line in f:
   if 'ATOM=Cd XPOS=' in line:
      aa=line.split() # N.B. string.split() method
      bb_2=float(aa[2])*fa
      bb_3=float(aa[3])*fb
      bb_4=float(aa[4])*fc
      bb_2=str(bb_2)
      bb_3=str(bb_3)
      bb_4=str(bb_4)
      print bb_2
      print bb_3
      print bb_4
      g.write('Cd  '+bb_2+' '+bb_3+' '+bb_4+'\n')



   if 'ATOM=Si XPOS=' in line:
      aa=line.split() # N.B. string.split() method
      bb_2=float(aa[2])*fa
      bb_3=float(aa[3])*fb
      bb_4=float(aa[4])*fc
      bb_2=str(bb_2)
      bb_3=str(bb_3)
      bb_4=str(bb_4)
      print bb_2
      print bb_3
      print bb_4

      g.write('Si  '+bb_2+' '+bb_3+' '+bb_4+'\n')


   if 'ATOM=N  XPOS=' in line:
      aa=line.split() # N.B. string.split() method
      bb_2=float(aa[2])*fa
      bb_3=float(aa[3])*fb
      bb_4=float(aa[4])*fc
      bb_2=str(bb_2)
      bb_3=str(bb_3)
      bb_4=str(bb_4)
      print bb_2
      print bb_3
      print bb_4

      g.write('N   '+bb_2+' '+bb_3+' '+bb_4+'\n')
f.close()
g.close()
