# Flight Ticket analysis based on a US Dataset

I analysed this dataset: https://www.kaggle.com/datasets/dilwong/flightprices

the `final_analysis.ipynb` **jupyter notebook** is using the 2 million version of this dataset

# Run the project by Yourself: 

1. dowload the snappy parquet version of the dataset
   - https://www.dropbox.com/scl/fo/mybc5v9s800orsu78b6ao/h?rlkey=1an4ndcscd5uw9yi7oxx8ypfn&e=1&dl=0
2.  go to `Scripts` -> `flights_data.py` and change the following line:
   ```python
      # change the path to your own path
      in_path = glob('/Users/alialshaikh/Downloads/itineraries_snappy.parquet')[0]

      # and change the slice number to suit the number of rows you want to process
      # or num of rows you want to work with

      
      # Slice the first 1,000,000 rows efficiently
      df = df.slice(0, 1_000_000)

   ```

3. here you have 2 options after this point:


   3.1. go to `Scripts` -> `final-analysis.py` and `RUN IT`, using `python3 final-analysis.py` -- This will take time to run, depending on your dataset size ex. 2_000_000, it may take up to 60 seconds so don't worry. put an eye the `Memory Pressure`, or the `RAM`.


   3.2. OR use the jupyter notebook `final_analysis.ipynb` and change the following cell:

      ```pyhton
         # loaded at the end
         df = pd.read_csv('final_data_2m.csv')

         # CHANGE IT TO ☕️
         df = pd.read_csv('final_data.csv')
      ```


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

or `pip install seaborn pyarrow polars` in the `terminal` or in the `cmd`

4. Use Good RAM

5. HAPPY CODING 😉



# Thank You & Have a Wonderful Exploration ☕️
## RAMADAN MUBARAK 🌙
