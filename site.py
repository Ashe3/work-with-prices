from datetime import datetime
from utils import parse_xls, drop_cols, filter_rows, get_rest, write_file

date = datetime.today()
file = 'sitePrice.xls'
cols = [x for x in range(8)]
names = ['code', 'product_name', 'k_opt', 'opt', 'discount', 'retail', 'reserved', 'rest']
out_file = 'SitePriceOutput{}.{}.{}.xls'.format(date.day, date.month, date.year)

df = parse_xls(file, cols, names)
df = filter_rows(df)
df = get_rest(df)

try:
  write_file(df, out_file)
  print('work is done')
  print('price writed as {}'.format(out_file))
except expression as identifier:
  print('Try again')
  print(identifier)