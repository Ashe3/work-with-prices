from datetime import datetime
from utils import parse_xls, drop_cols, filter_rows, get_rest, write_file, set_vat

date = datetime.today()
file = 'traderPrice.xls'
cols = [x for x in range(8)]
names = ['product_name', 'purchase', 'purchase_r', 'opt', 'discount', 'retail', 'reserved', 'rest']
to_drop = ['purchase', 'purchase_r', 'discount', 'retail']
VAT = ['kormoran', 'kleber']
out_file = 'PriceOutput{}.{}.{}.xls'.format(date.day, date.month, date.year)

df = parse_xls(file, cols, names)
drop_cols(df, to_drop)
df = filter_rows(df)
df = get_rest(df)
set_vat(df, VAT)

try:
  write_file(df, out_file)
  print('work is done')
  print('price writed as {}'.format(out_file))
except expression as identifier:
  print('Try again')
  print(identifier)