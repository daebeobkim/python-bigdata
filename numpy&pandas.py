import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


print("\n\n                                            The Chart Below is NBA average stats\n\n")
NBA_stat = pd.read_excel('C:/Users/rlaeo/OneDrive/바탕 화면/플잭/NBA_stats.xlsx')
NBA_stat_sorted = NBA_stat.sort_values(by='Season', ascending = True) #season을 기준으로 오름차순 정렬
print(NBA_stat)
print("\n\n                                            The Chart Below is Ray Allen's NBA career stats\n\n")
Allen_stat = pd.read_excel('C:/Users/rlaeo/OneDrive/바탕 화면/플잭/Ray_Allen_average.xlsx')
print(Allen_stat)
print('\nFirstly I will extract important columns from NBA stats\n')
NBA_want = pd.read_excel('C:/Users/rlaeo/OneDrive/바탕 화면/플잭/NBA_stats.xlsx')
NBA_want_sorted = NBA_want.sort_values(by='Season', ascending = True)
print(NBA_want)


NBA_season = NBA_want_sorted['Season']
NBA_weight = NBA_want_sorted['Wt']


plt.figure(figsize=(40,20))
plt.plot(NBA_season, NBA_weight, color = 'red', linestyle='dashed', marker = 'o', markerfacecolor ='blue', markersize=10, lw=4)
plt.xlabel('Season', size =20)
plt.ylabel('Player Weight', size = 20)
plt.title('NBA Player Weight Change', size=30)
plt.xticks(rotation = 90)
plt.grid()
plt.show()