import globals as glb
import utils as utl

df = glb.pd.read_csv("sales_data_sample.csv", encoding='ISO-8859-1')

# Data Cleaning
df['ORDERDATE'] = utl.clean_dates(df)

# Apology emails
utl.send_apology_email(df)

# Country sales
utl.country_sales(df)

# Month sales
utl.month_trending_sales(df, '2003-01-01', '2005-06-1')

print("Analysis Done.")
