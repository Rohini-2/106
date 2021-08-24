import csv
import numpy as np
days=[]
marks=[]
with open ("Student Marks vs Days Present.csv.txt") as f:
  df=csv.DictReader(f)
  for i in df:
    days.append(float(i["Days Present"]))
    marks.append(float(i["Marks In Percentage"]))

dataCR=np.corrcoef(days,marks)
print(dataCR)