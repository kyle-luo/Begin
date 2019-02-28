import pandas as pd
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO
import time

# Load the data in pandas
df = pd.read_csv('C:/Users/tsjlk/OneDrive/Desktop/test.csv', low_memory=False)

print (df.head(10))

print (df.info())

print (df.shape)

date = df['Issue Date']
idate = []
for day in date:
    idate.append(day)
idx = pd.to_datetime(idate)
new = pd.Series(idx.to_period('m'))

datecount = new.value_counts().sort_index().reset_index()
datecount.columns = ['Date','Count']
datecount.Date = datecount.Date.dt.strftime('%Y-%m')
print (datecount)

df['Issue Date'] = pd.to_datetime(df['Issue Date'])
df = df.sort_values(by='Issue Date', ascending=True)
print (df.head(10))

