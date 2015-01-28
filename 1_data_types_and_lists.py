from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import os

main_dir = "/Users/jseidenfeld/Desktop/Data"
git_dir = "/Users/jseidenfeld/Documents/School/Classes/Big Data for Energy 590/BigData590GitHubJS/PubPol590GitHubJS"
csv_file_good = "sample_data_clean.csv"
csv_file_bad = "/sample_data_clean.csv"

df = pd.read_csv(os.path.join(main_dir, csv_file_bad))
df = pd.read_csv(os.path.join(main_dir, csv_file))

# PYTHON DATA TYPES

## strings
str1 = "hello, computer"
str2 = "hello, human"
str3 = u"eep"

type(str1)
type(str2)
type(str3)

## numeric
int1 = 10
float1 = 22.56
long1 = 32950995309309883000009999

## logical
bool1 = True
notbool1 = 0
bool2 = bool(notbool1)

# Creating Lists and Tuples

## Lists can be changed; Tuples cannot. We almost exclusively use lists.

list1 = []
list
list2 = [7,8,"a"]
list2[2] ## outputs the number "3" because item number 2 is 
list2[2] = 5
list2[2]

## tuples, which can't be changed; parentheses denote tuples
tup1 = (8,3,19)
tup1[2]

## you can convert lists to tuples and vice versa; can convert most things into lists
tup2 = tuple(list1)

### lists can be appended and extended
list2 = [8, 3, 19]
list2.append([3,90])
len(list2)
list3 = [8, 3, 19]
list3.extend([6, 88])
len(list3)

## CONVERTING LISTS TO SERIES AND DATAFRAME
list4 = range(5,10) ## range(n,m) give a list from n to m-1
list5 = range(5) ## gives list from 0 to m-1
list5




