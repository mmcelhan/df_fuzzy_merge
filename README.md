#df_fuzzy_merge
fuzzy merge for pandas dataframe package

##local install:
pip install git+https://github.com/mmcelhan/df_fuzzy_merge.git#egg=df_fuzzy_merge

## to test:
import df_fuzzy_merge as df
import os
import pandas as pd

first_df = pd.read_csv(os.path.join("testing_files", "data_1.csv"))
second_df = pd.read_csv(os.path.join("testing_files", "data_2.csv"))

merged_df = df.df_fuzzy_merge(first_df, second_df, left_on=['last_name', 'first_name', 'school'], right_on=['first_name', 'school', 'last_name'])
print(merged_df)

## source code available here:
https://github.com/mmcelhan/dataframe_fuzzy_merge_source
