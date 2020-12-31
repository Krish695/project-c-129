import pandas as pd
import csv

file1= "bright_stars.csv"
file2="dwarf_stars.csv"

d1=[]
d2=[]
with open (file1,'r',encoding="utf8")as f:
    csv_reader=csv.reader(f)
    for i in csv_reader:
        d1.append(i)

with open (file2,'r',encoding="utf8")as f:
    csv_reader=csv.reader(f)
    for i in csv_reader:
        d2.append(i)

h1 = d1[0]
h2 = d2[0]
t_d1=d1[1:]
t_d2=d2[1:]
h=h1+h2
p_d=[]
for i in t_d1:
    p_d.append(i)

for i in t_d2:
    p_d.append(i)

with open ("total_stars.csv",'w',encoding="utf8")as f:
    csv_writer=csv.writer(f)
    csv_writer.writerow(h)
    csv_writer.writerows(p_d)
df=pd.read_csv('total_stars.csv')

