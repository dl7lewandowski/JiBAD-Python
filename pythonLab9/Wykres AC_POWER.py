import pandas as pd 
from matplotlib import pyplot as plt 
import datetime
dateparse1 = lambda x: datetime.datetime.strptime(x, '%d-%m-%Y %H:%M')
dateparse2 = lambda x: datetime.datetime.strptime(x, '%Y-%m-%d %H:%M:%S')

data1 = pd.read_csv('/Users/dl7le/Plant_1_Generation_Data.csv',  parse_dates = ["DATE_TIME"], date_parser=dateparse1)
data2 = pd.read_csv("/Users/dl7le/Plant_2_Generation_Data.csv",  parse_dates = ["DATE_TIME"], date_parser=dateparse2)

data = pd.concat([data1, data2])

# pkt 1
# tydzien 15-05-2020 00:00 : 22-05-2020 00:00

startDate = datetime.datetime(year=2020, month=5, day=15, hour=0, minute=0, second=0)
endDate = datetime.datetime(year=2020, month=5, day=22, hour=0, minute=0, second=0)

# 5 wybranych generatorow w tym tygodniu
dateMask = (data['DATE_TIME'] > startDate) & (data['DATE_TIME'] <= endDate)

week = data.loc[dateMask]
frame1 = week.loc[week["SOURCE_KEY"] == "1BY6WEcLGh8j5v7"]
frame2 = week.loc[week["SOURCE_KEY"] == "1IF53ai7Xc0U56Y"]  # DRY
frame3 = week.loc[week["SOURCE_KEY"] == "3PZuoBAID5Wc2HD"]
frame4 = week.loc[week["SOURCE_KEY"] == "7JYdWkrLSPkdwr4"]
frame5 = week.loc[week["SOURCE_KEY"] == "McdE0feGgRqW7Ca"]
frame6 = week.loc[week["SOURCE_KEY"] == "VHMLBKoKgIrUVDU"]

fig, axs = plt.subplots(3,2)
fig.suptitle('AC_POWER')

# rysowanie wykresu

f1_x = frame1["DATE_TIME"].tolist() # Lista? Czemu nie DataFrame?
f1_y = frame1["AC_POWER"].tolist()
axs[0,0].plot(f1_x, f1_y, linewidth=1)
axs[0,0].set_title("1BY6WEcLGh8j5v7")

f2_x = frame2["DATE_TIME"].tolist() # DRY
f2_y = frame2["AC_POWER"].tolist()
axs[0,1].plot(f2_x, f2_y, linewidth=1)
axs[0,1].set_title("1IF53ai7Xc0U56Y")

f3_x = frame3["DATE_TIME"].tolist()
f3_y = frame3["AC_POWER"].tolist()
axs[1,0].plot(f3_x, f3_y, linestyle="--", linewidth=1)
axs[1,0].set_title("3PZuoBAID5Wc2HD")

f4_x = frame4["DATE_TIME"].tolist()
f4_y = frame4["AC_POWER"].tolist()
axs[1,1].plot(f4_x, f4_y, linestyle="--", linewidth=1)
axs[1,1].set_title("7JYdWkrLSPkdwr4")

f5_x = frame5["DATE_TIME"].tolist()
f5_y = frame5["AC_POWER"].tolist()
axs[2,0].plot(f5_x, f5_y, linestyle="--", linewidth=1)
axs[2,0].set_title("McdE0feGgRqW7Ca")

f6_x = frame6["DATE_TIME"].tolist()
f6_y = frame6["AC_POWER"].tolist()
axs[2,1].plot(f6_x, f6_y, linestyle="--", linewidth=1)
axs[2,1].set_title("VHMLBKoKgIrUVDU")

plt.show()


