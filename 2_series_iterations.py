from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import os

main_dir = "/Users/jseidenfeld/Desktop/Data"
git_dir = "/Users/jseidenfeld/Documents/School/Classes/Big Data for Energy 590/BigData590GitHubJS/PubPol590GitHubJS"
csv_file = "sample_data_clean.csv"

# FOR LOOPS ----------------------
df = pd.read_csv(os.path.join(main_dir, csv_file))

list1 = range(10,15)
list2 = ['a','b','c']
list3 = [1, 'a', True]

## iterating over elements (for loops)
for v in list1:
    v 
    
for v in list2:
    print(v) 

for v in list3:
    print(v,type(v)) 
    
    
for v in list3:
    print(v,type(v), 'haha') 
    
### populating (empty) lists
list1 ## is all integers
list4 = [] ## empty list
list5 = []

for v in list1:
    v2 = v**2
    list4.extend([v2])
    list5.append(v2)
    
[v**2 for v in list1]
    
list6 = [ v**2 < 144 for v in list1]

## iterating using enumerate
list7 = [ [i, v/2] for i, v in enumerate(list1)]

## iterate through a series ---------------
s1 = df['consump']
[v > 2 for v in s1]

[[i,float(v)*.3] for i, v in s1.iteritems()]

# ITERATE THROUGH DATAFRAME
[v for v in df]
[df[v] for v in df]
[[i, v] for i, v in df.iteritems()]