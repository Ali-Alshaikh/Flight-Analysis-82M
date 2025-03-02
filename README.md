# Flight Ticket analysis based on a US Dataset

I analysed this dataset: https://www.kaggle.com/datasets/dilwong/flightprices

the .ipynb jupyter notebook is using the 2 million version of this dataset


1. you can dowload the snappy parquet version of the dataset, and then use the flights_data.py to generate the size of rows you desire: "2 million or 3 million or etc. "
   link to snappy parquet: https://www.dropbox.com/scl/fo/mybc5v9s800orsu78b6ao/h?rlkey=1an4ndcscd5uw9yi7oxx8ypfn&e=1&dl=0

2. then you can use the `final-analysis.py` to generate the graphs to your system. OR use the `final analysis jupyter notebook` to make this project work 😊

# Requirments 
1. python
2. The following imports:
  ```python
      import pandas as pd
      import matplotlib.pyplot as plt
      import seaborn as sns
      import matplotlib.ticker as mticker
      import os
      import time
      from glob import glob
      import pyarrow.parquet as pq
      import polars as pl
   ```

I think most of the lad's reading this already have all these imports, but may miss the following: 
1. polars - use --> `pip install polars`
2. pyarrow - use --> `pip install pyarrow`
3. seaborn - use --> `pip install seaborn`

or `pip install seaborn pyarrow polars` in the terminal or in the `cmd`

4. HAPPY CODING 😉



# Thank You & Have a Wonderful Exploration ☕️
## RAMADAN MUBARAK 🌙
