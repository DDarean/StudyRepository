import pandas as pd
import os

# folder path
dir_path = r'data/'

# list to store files
res = []

# Iterate directory
for path in os.listdir(dir_path):
    # check if current path is a file
    if os.path.isfile(os.path.join(dir_path, path)):
        res.append(path)
print(res)

for file in res:
    data = pd.read_csv(f'data/{file}')
    data.to_parquet(f'{file}.parquet', compression="gzip")