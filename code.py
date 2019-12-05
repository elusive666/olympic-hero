# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
path
#Code starts here
data = pd.read_csv(path)
data.rename(columns = {'Total':'Total_Medals'}, inplace = True)
print(data.head())


# --------------
#Code starts here





data['Better_Event'] = np.where(data['Total_Summer'] == data['Total_Winter'], 'Both', 
(np.where(data['Total_Summer'] > data['Total_Winter'], 'Summer', 'Winter')))

#data['Better_Event'] = np.where(data['Total_Summer'] > data['Total_Winter'], 'Summer', 'Winter')
#data['Better_Event'] =np.where(data['Total_Summer'] ==data['Total_Winter'],'Both',data['Better_Event']) 
print(data.head())
better_event = data['Better_Event'].value_counts().idxmax()
print(better_event)


# --------------
#Code starts here
top_countries = data[['Country_Name','Total_Summer', 'Total_Winter','Total_Medals']]
print(top_countries.head())
top_countries.drop(index = len(top_countries)-1, axis = 0, inplace = True)
def top_ten(tempDF, tempCol):
    country_list=[]
    top_10 = tempDF.nlargest(10, tempCol)
    country_list = list(top_10['Country_Name'])
    return country_list

top_10_summer = top_ten(top_countries, 'Total_Summer')
#print(top_10_summer)
top_10_winter = top_ten(top_countries, 'Total_Winter')
#print(top_10_winter)
top_10 = top_ten(top_countries, 'Total_Medals')
#print(top_10)
tempSetList = list(set(top_10_summer + top_10_winter + top_10))
#print(tempSetList)
common = []
if(set(top_10_summer) & set(top_10_winter) & set(top_10)):
    common.append(list(set(top_10_summer) & set(top_10_winter) & set(top_10)))
    common = common[0]
print(common)


# --------------
#Code starts here
summer_df = data[data['Country_Name'].isin(top_10_summer)]
winter_df = data[data['Country_Name'].isin(top_10_winter )]
top_df = data[data['Country_Name'].isin(top_10)]
print(top_df)


# --------------
#Code starts here
summer_df['Golden_Ratio'] = summer_df['Gold_Summer']/summer_df['Total_Summer']
temploc = summer_df['Golden_Ratio'].idxmax()
summer_max_ratio = summer_df.loc[temploc].Golden_Ratio
summer_country_gold = summer_df.loc[temploc].Country_Name
print(summer_max_ratio , summer_country_gold)
winter_df['Golden_Ratio'] = winter_df['Gold_Winter']/winter_df['Total_Winter']
temploc = winter_df['Golden_Ratio'].idxmax()
winter_max_ratio = winter_df.loc[temploc].Golden_Ratio
winter_country_gold = winter_df.loc[temploc].Country_Name
print(winter_max_ratio , winter_country_gold)
top_df['Golden_Ratio'] = top_df['Gold_Total']/top_df['Total_Medals']
temploc = top_df['Golden_Ratio'].idxmax()
top_max_ratio = top_df.loc[temploc].Golden_Ratio
top_country_gold = top_df.loc[temploc].Country_Name
print(top_max_ratio , top_country_gold)


# --------------
#Code starts here
data.drop(index = len(data)-1, axis = 0, inplace = True)
data_1 = data
data_1['Total_Points'] = data_1.Gold_Total*3 + data_1.Silver_Total*2 + data_1.Bronze_Total
tempIndex = data_1['Total_Points'].idxmax()
most_points = data_1.loc[tempIndex].Total_Points
best_country = data_1.loc[tempIndex].Country_Name
print(most_points, best_country)


# --------------
#Code starts here
best = data[data['Country_Name'] == best_country]
best = best[['Gold_Total','Silver_Total','Bronze_Total']]
print(best.head())


