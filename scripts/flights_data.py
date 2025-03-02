import pandas as pd, numpy as np
from glob import glob
import pyarrow.parquet as pq
import pandas as pd
import polars as pl
import time


s = time.time()
print(f'started......')

in_path = glob('/Users/alialshaikh/Downloads/itineraries_snappy.parquet')[0]


# Load the Parquet file using Polars (faster than Pandas)
df = pl.read_parquet(in_path)

# Slice the first 2,000,000 rows efficiently
df = df.slice(0, 1_000_000)

# Save to CSV efficiently (Polars is much faster than Pandas)
df.write_csv(f'final_data.csv')


e = time.time()

t = e - s

print(f'total time taken {t:.2f} s')
