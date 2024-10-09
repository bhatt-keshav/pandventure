# Creates a series of dates with a frequency of 1 month
pd.date_range(start='1/1/2024', periods=12, freq='M')

# Creates a daily series. Note the format can either be with / or -
date_series = pd.date_range(start='2022-12-01', end=today, freq='D')
