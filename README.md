# Flight Ticket analysis based on a US Dataset

I analysed this dataset: https://www.kaggle.com/datasets/dilwong/flightprices

the `final_analysis.ipynb` **jupyter notebook** is using the 2 million version of this dataset

# Exploration Notebooks (folder)
- contains the exploration notebooks used to do the **EDA** (Exploratory data analysis) thingy, take a look if you want

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

# Presentation Mode using (RISE)

1. `pip install rise`
   - Look at this link to see how to deal with rise: https://rise.readthedocs.io/en/latest/usage.html#creating-a-slideshow
2. How to change the cells to: `slide` , `sub-slide`, `fragment`, etc. :
     ![Screenshot 2025-03-02 at 5 20 08 PM](https://github.com/user-attachments/assets/8c4b91ed-ab67-4787-bcf2-1f755e6609b8)

   ![Screenshot 2025-03-02 at 5 19 01 PM](https://github.com/user-attachments/assets/5d30900b-c13f-4dc9-9dc5-d375a37ea186)

![Screenshot 2025-03-02 at 5 19 33 PM](https://github.com/user-attachments/assets/7e773b0b-da91-4f29-8cf7-9535f9d3ea82)

   

# Thank You & Have a Wonderful Exploration ☕️
## RAMADAN MUBARAK 🌙
