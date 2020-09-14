'''
Merge files into excel file

Author: Alexander Wu
Date: 9/13/20

## Usage

input.txt ignores empty lines and assumes the following format:

```
sheet_name
file1.csv
file2.csv

sheet_name
file1.csv
file2.csv
```

## Requirements

* pandas: `pip install --user pandas`
* openpyxl: `pip install --user openpyxl`
'''
import pandas as pd

# Export .xlsx without bold headers
import pandas.io.formats.excel
pandas.io.formats.excel.ExcelFormatter.header_style = None

INPUT_FILE = 'input.txt'
OUTPUT_PATH = 'merged.xlsx'

with open(INPUT_FILE, 'r') as f:
    input_lines = f.readlines()

input_list = [x.strip() for x in input_lines if x.strip()]

sheet_names = [x for i, x in enumerate(input_list) if i % 3 == 0]
file1_names = [x for i, x in enumerate(input_list) if i % 3 == 1]
file2_names = [x for i, x in enumerate(input_list) if i % 3 == 2]

with pd.ExcelWriter(OUTPUT_PATH) as writer:
    for sheet_name, file1, file2 in zip(sheet_names, file1_names, file2_names):
        print(sheet_name, file1, file2)
        file1_df = pd.read_csv(file1)
        file2_df = pd.read_csv(file2)
        file1_df[''] = None
        sheet_df = pd.concat([file1_df, file2_df], axis=1)
        sheet_df.to_excel(writer, sheet_name=sheet_name, index=False)
