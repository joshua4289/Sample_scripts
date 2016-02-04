#!/usr/bin/python
from __future__ import print_function
import os
import numpy as np
import sys




abs_path=os.path.abspath(__file__) #path of the current script file
dir_path=os.path.dirname(abs_path) #directory name
os.chdir(dir_path)

#Making a CSV file from the pdb_file given



pdb_str=str(sys.argv[1])
pdb_file_ori=open(pdb_str)
pdb_file=open('cordinates_all.csv')

x_new_file=open('x_new_cordinates.txt','w+')
y_new_file=open('y_new_cordinates.txt','w+')
z_new_file=open('z_new_cordinates.txt','w+')
new_cordinate_file=open ('all_new_cordinates.txt','w+')


cordinates=np.genfromtxt(pdb_file,delimiter=",")



#slicing each "column" on the basis of X ,Y and Z cordinates
x=cordinates[:,][:,0]
y=cordinates[:,][:,1]
z=cordinates[:,][:,2]


x_max=max(x)
x_min=min(x)

cx=(x_max-x_min)/2.0

x_max=max(x)
x_min=min(x)

cx=(x_max-x_min)/2.0

y_max=max(y)
y_min=min(y)

cy=(y_max-y_min)/2.0

z_max=max(z)
z_min=min(z)

cz=(z_max-z_min)/2.0

#list of centre cordinates
#cxyz=[cx,cy,cz]


print(len(x),len(y),len(z))

for count,elem in enumerate(y):

  x_val =format((x[count]-cx)*1.05,'.3f')
  print(str(x_val).rjust(7,' '),file=x_new_file)
  x_new_file.flush()
  y_val =format((y[count]-cy)*1.05,'.3f')
  print(str(y_val).rjust(7,' '),file=y_new_file)
  y_new_file.flush()
  z_val =format((z[count]-cx)*1.05,'.3f')
  print(str(z_val).rjust(7,' '),file=z_new_file)

pdb_first_columns =open('pdb_first_columns.txt','w+')
pdb_last_columns=open('pdb_last_columns.txt','w+')

for line in pdb_file_ori:
    print (line[0:4]+line[4:11]+line[11:16]+line[16:20]+line[20:24]+line[24:31],file=pdb_first_columns)
    print (line[55:80],file=pdb_last_columns)

