import datetime
import time
import pandas as pd


def Download_crypto_data(Currency):
  Starting_date=input('Data since date: (dd-mm-yyyy format.)\n').split('-')
  Ending_date=input('Data until date: (dd-mm-yyyy format.)').split('-')
  #datetime.datetime is a combination of date and time, then timetuple returns a tuple of type time.struct_time, which in turn is made by time.mktime to seconds.
  #(the tuple needs to be type time.struct_time), also the number of seconds is given as a float, so we turn it into int.
  period_start=int(time.mktime(datetime.datetime(int(Starting_date[2]),int(Starting_date[1]),int(Starting_date[0]), 23 ,59).timetuple()))
  period_end=int(time.mktime(datetime.datetime(int(Ending_date[2]),int(Ending_date[1]),int(Ending_date[0]), 23 ,59).timetuple()))
  interval = '1d' #Frequency, you can also ask that if you want.

  url=f'https://query1.finance.yahoo.com/v7/finance/download/{Currency}?period1={period_start}&period2={period_end}&interval={interval}&events=history&includeAdjustedClose=true'
  df=pd.read_csv(url)#defines the csv file
  df.to_csv(f'{Currency}.csv')#saves it and names it as the currency
