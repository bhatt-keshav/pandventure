## PICKLING
import pickle

a = {'hello': 'world'}

# Write to pickle
with open('filename.pickle', 'wb') as handle:
    pickle.dump(a, handle, protocol=pickle.HIGHEST_PROTOCOL)

# Read from pickle
with open('filename.pickle', 'rb') as handle:
    b = pickle.load(handle)

## PARQUETTING
# write
df.to_parquet('df.parquet.gzip', compression='gzip')
# read
df = pd.read_parquet('df.parquet.gzip')
