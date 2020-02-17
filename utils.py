import pandas as pd
from math import isnan

filters = ['б/у', '@', 'износ']

def parse_xls(filename, cols, names):
  df = pd.read_excel(filename, header=8, usecols=cols, names=names)
  return df

def drop_cols(df, cols):
  df.drop(cols, inplace=True, axis=1)

def filter_rows(df):
  df.replace({'-': 0}, inplace=True)
  booleans = []

  for index, row in df.iterrows():
    if type(row.opt) == str or isnan(row.opt):
      booleans.append(False)
    elif any(value in row.product_name.__str__() for value in filters):
      booleans.append(False)
    else:
      booleans.append(True)

  is_Valid = pd.Series(booleans)
  df = df[is_Valid]

  return df

def get_rest(df):
  df['free'] = df['rest'] - df['reserved']
  df = df[df.free > 0]
  return df.drop(['reserved', 'rest'], axis=1)

def set_vat(df, VAT):
  available = []
  for index, row in df.iterrows():
    if any(v in row.product_name.__str__().lower() for v in VAT):
      available.append(row.opt * 1.05)
    else:
      available.append('-')

  df.insert(2, 'VAT', available, True)

def write_file(df, filename):
  df.to_excel(filename, index = False, header = False)
