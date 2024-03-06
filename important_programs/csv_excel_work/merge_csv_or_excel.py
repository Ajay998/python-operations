import glob
import pandas as pd
import warnings
# list all csv files only

# ++++++++++++++++++++++++Csv file+++++++++++++++++++++++++++++++++++++++++++++++
csv_files = glob.glob('*.{}'.format('csv'))
print(csv_files)
print(len(csv_files))
df = pd.concat(map(pd.read_csv, csv_files), ignore_index=True)
print(df)
df.to_csv("completed_csv_files.csv")

# ++++++++++++++++++++++++Excel file+++++++++++++++++++++++++++++++++++++++++++++++

# excel_files = glob.glob('*.{}'.format('xlsx'))
# print(excel_files)
# df = pd.concat(map(pd.read_excel, excel_files), ignore_index=True)
# print(df)
# df.to_csv("completed_excel_files.xlsx")


