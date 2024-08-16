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

# Second use case with transform
# Same output as above, but the series length is same as that of the original df
# Whereas the first case would have given a much reduced df with nrows = unique group by elements

df.groupby(by='Date')[['Mata', 'Data']].transform(sum)

# To create staggered grouping, use multiple group by columns
df.groupby(by=['Date', 'Data']).sum()
