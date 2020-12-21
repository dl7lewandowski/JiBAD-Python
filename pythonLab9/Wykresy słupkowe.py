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
print(date)
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
            


y1 = [0 for i in range(7)]   
y2 = [0 for i in range(7)]
x = ["<75%", "75-85%", "85-95%", "95-105%", "105-115%", "115-125%", ">125%"]


for e in means:
    if e[-3] != 0:  # pomijamy takie dni w ktorych srednia byla 0 
        ratio = e[-2] / e[-3]
        if ratio < 0.75:
            y1[0]+=1
        elif ratio < 0.85:
            y1[1] += 1
        elif ratio < 0.95:
            y1[2] += 1
        elif ratio < 1.05:
            y1[3] += 1
        elif ratio < 1.15:
            y1[4] += 1
        elif ratio <= 1.25:
            y1[5] += 1
        else:
            y1[6] += 1

for e in means:
    if e[-3] != 0:  
        ratio = e[-1] / e[-3]
        if ratio < 0.75:
            y2[0]+=1
        elif ratio < 0.85:
            y2[1] += 1
        elif ratio < 0.95:
            y2[2] += 1
        elif ratio < 1.05:
            y2[3] += 1
        elif ratio < 1.15:
            y2[4] += 1
        elif ratio <= 1.25:
            y2[5] += 1
        else:
            y2[6] += 1

fig, (ax1, ax2) = plt.subplots(2)
fig.suptitle('days with daily yield to mean ratio')

ax1.bar(x, y1)
ax1.set_title("z9Y9gH1T5YWrNuG")
ax2.bar(x, y2)
ax2.set_title('7JYdWkrLSPkdwr4')
print(means)
plt.show()
