'''
Merge files into excel file

Author: Alexander Wu
Date: 9/13/20

Requirements:

* pandas: `pip install pandas`
'''
import pandas as pd
import pandas.io.formats.excel
pandas.io.formats.excel.ExcelFormatter.header_style = None

INPUT_FILE = 'input.txt'
OUTPUT_PATH = 'merged.xlsx'

input_df = pd.read_csv('input.txt', header=None)
input_list = input_df[0].values

dir1_file1_df = pd.read_csv(input_list[0])
dir1_file2_df = pd.read_csv(input_list[1])
dir2_file1_df = pd.read_csv(input_list[2])
dir2_file2_df = pd.read_csv(input_list[3])
dir3_file1_df = pd.read_csv(input_list[4])
dir3_file2_df = pd.read_csv(input_list[5])
dir4_file1_df = pd.read_csv(input_list[6])
dir4_file2_df = pd.read_csv(input_list[7])

dir1_file1_df[''] = None
sheet1_df = pd.concat([dir1_file1_df, dir1_file2_df], axis=1)
dir2_file1_df[''] = None
sheet2_df = pd.concat([dir2_file1_df, dir2_file2_df], axis=1)
dir3_file1_df[''] = None
sheet3_df = pd.concat([dir3_file1_df, dir3_file2_df], axis=1)
dir4_file1_df[''] = None
sheet4_df = pd.concat([dir4_file1_df, dir4_file2_df], axis=1)

with pd.ExcelWriter(OUTPUT_PATH) as writer:
    sheet1_df.to_excel(writer, sheet_name='Sheet1', index=False)
    sheet2_df.to_excel(writer, sheet_name='Sheet2', index=False)
    sheet3_df.to_excel(writer, sheet_name='Sheet3', index=False)
    sheet4_df.to_excel(writer, sheet_name='Sheet4', index=False)
