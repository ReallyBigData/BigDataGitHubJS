from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import os

main_dir = "/Users/jseidenfeld/Documents/School/Classes/Big Data for Energy 590/Panda Repositories/LiveDemo/"
csv_file = "Data/sample_missing.csv"

# Importing Data: Setting Missing Values (Sentinels) 

df = pd.read_csv(os.path.join(main_dir, csv_file))
df.head() # top 5 values
df.head(10) # head(n) gives top n rows
df[:10]
df.tail(10) # tail(n) gives bottom n values
df['consump'].head(10).apply(type) # apply function 'type' to top 10 rows of consump


## we DONT want string data. periods '.' are common place holders for missing data in stata, etc. need to create new 
## missing value sentineles ot adjust. a sentinel is a placeholder for missing or bad data
missing = ['.', 'NA', 'NULL', '']
df = pd.read_csv(os.path.join(main_dir, csv_file), na_values = missing)
df.head(10)
df['consump'].head(10).apply(type)
## NaN = "not a number"

# MISSING DATA (USING SMALLER DATAFRAME) --------------------------------------

# Quick tip: you can repead lists by multiplying!

[1,2,3]
[1,2,3]*3

# types of missing data:
None
np.nan
type(None)
type(np.nan)

## create sample data set
zip1 = zip([2,4,8], [np.nan, 5, 5], [np.nan, np.nan, 221])
df1 = DataFrame(zip1, columns = ['a', 'b', 'c'])


## search for missing data
df1.isnull() # pandas method to find missing data
np.isnan(df1) # numpy way

## subset of columns
cols = ['a', 'c']
df1[cols]
df1[cols].isnull()

## for series
df1['b'].isnull()

## find non-missing values
df1.notnull()
df1.isnull()
df1.isnull() == df1.notnull()


# Filling in or dropping values
# pandas method 'fillna'
df1.fillna(999)
df2 = df1.fillna(999)

## pandas method 'dropna'
df1.dropna() ## by default, drops ROWS with ANY missing values
df1.dropna(axis = 0, how = 'any') # explicility states defaults
df1.dropna(axis = 1, how = 'any') # drop COLUMNS with ANY missing values
df1.dropna(axis = 0, how = 'all') # drop ROWS with ALL missing values

## try it out with df
df.dropna(how = 'all') ## don't need to specify axis since it's default

## SEE ROWS WITH MISSING DATA -----------------------------
df1.isnull()