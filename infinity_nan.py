df.replace([np.inf, -np.inf], np.nan, inplace=True)
ds = df.isin([np.inf, -np.inf]) 
