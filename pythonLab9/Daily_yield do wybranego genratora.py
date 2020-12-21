import pandas as pd
import matplotlib.pyplot as plt
import datetime


dateparse1 = lambda x: datetime.datetime.strptime(x, '%d-%m-%Y %H:%M')
dateparse2 = lambda x: datetime.datetime.strptime(x, '%Y-%m-%d %H:%M:%S')

data1 = pd.read_csv('/Users/dl7le/Plant_1_Generation_Data.csv',  parse_dates = ["DATE_TIME"], date_parser=dateparse1)
data2 = pd.read_csv("/Users/dl7le/Plant_2_Generation_Data.csv",  parse_dates = ["DATE_TIME"], date_parser=dateparse2)

frame = pd.concat([data1, data2])



startDate = sorted(frame['DATE_TIME'].values.tolist())[0]

date = datetime.datetime.fromtimestamp(startDate / 1e9) - datetime.timedelta(hours=2, minutes=0) # poprawka na 2h po poprawnym parsowaniu danych na godzinę 00:00
#print(date)
endTime = sorted(frame['DATE_TIME'].values.tolist())[-1]
endTime = datetime.datetime.fromtimestamp(endTime / 1e9)
day = datetime.timedelta(hours=24, minutes=0)

means = []
while date <= endTime:
    date = date + day
    result = frame.loc[frame['DATE_TIME']==date]
    
    if result.empty == False:
        gen_row1 = result.loc[result['SOURCE_KEY']=='z9Y9gH1T5YWrNuG'].values.tolist()
        gen_row2 = result.loc[result['SOURCE_KEY']=='7JYdWkrLSPkdwr4'].values.tolist()
        if len(gen_row1) != 0 and len(gen_row2) != 0: # uwzgledniam tylko pelne zestawy danych
            means.append([date,result['DAILY_YIELD'].mean(),gen_row1[0][-2], gen_row2[0][-2]])
            


for e in means:
    if e[-2] != 0:
        print('data: ',e[0],'stousnek: ', e[-1]/e[-2])
    else:
        print(e[0],0)