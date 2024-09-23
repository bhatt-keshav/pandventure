# Initialize df
df = pd.DataFrame({
    "Date": [
        "2015-05-08", "2015-05-07", "2015-05-06", "2015-05-05",
        "2015-05-08", "2015-05-07", "2015-05-06", "2015-05-05"],
    "Data": [5, 8, 6, 1, 50, 100, 60, 120],
    "Mata": [15, 18, 16, 11, 510, 10, 601, 20],
})
df = df.sort_values('Date')

# Basic use case, give summary statistics
df.groupby(by='Date').sum()

# To perform an aggregation for a specific column do:
# You can use other grouping mechanisms besides sum for instance prod()
df.groupby('A')['C'].prod() # groups by A and does a product on C

# Use reset index to move the index to a column and make the grouped series a df
df_grouped = series_grouped.reset_index()

# To groupby without turning grouped by column into index
df.groupby(['col2','col3'], as_index=False).sum()

# Second use case with transform
# Same output as above, but the series length is same as that of the original df
# Whereas the first case would have given a much reduced df with nrows = unique group by elements

df.groupby(by='Date')[['Mata', 'Data']].transform(sum)

# To create staggered grouping, use multiple group by columns
df.groupby(by=['Date', 'Data']).sum()

# From SO [https://stackoverflow.com/questions/19523277/renaming-column-names-in-pandas-groupby-function]
df = pd.DataFrame({'A' : list('wwwwxxxx'), 
                   'B':list('yyzzyyzz'), 
                   'C':np.random.rand(8), 
                   'D':np.random.rand(8)})

   A  B         C         D
0  w  y  0.643784  0.828486
1  w  y  0.308682  0.994078
2  w  z  0.518000  0.725663
3  w  z  0.486656  0.259547
4  x  y  0.089913  0.238452
5  x  y  0.688177  0.753107
6  x  z  0.955035  0.462677
7  x  z  0.892066  0.368850
Let's say we want to group by columns A, B and aggregate column C with mean and median and aggregate column D with max. The following code would do this.

df.groupby(['A', 'B']).agg({'C':['mean', 'median'], 'D':'max'})
