# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import pandas as pd
import csv

df_a= pd.read_csv('a_lvr_land_a.csv')
df_b= pd.read_csv('b_lvr_land_a.csv')
df_e= pd.read_csv('e_lvr_land_a.csv')
df_f= pd.read_csv('f_lvr_land_a.csv')
df_h= pd.read_csv('h_lvr_land_a.csv')

df_all=(pd.concat([df_a,df_b,df_e,df_f,df_h],axis=0,join='outer'))#合併所需csv
df_all=df_all.drop(df_all[df_all.鄉鎮市區=="The villages and towns urban district"].index)#刪除英文標題列
#df_all.to_csv('df_all2.csv')


filter1 = (df_all["主要用途"] == "住家用")
filter2 = (df_all["建物型態"].str.contains('住宅大樓', na=False))
filter3 = (df_all["總樓層數"].str.contains('十', na=False))

df_all_filt=df_all[(filter1&filter2&filter3)]

df_all_filt=df_all_filt.drop(df_all_filt[df_all_filt.總樓層數=="十層"].index)
df_all_filt=df_all_filt.drop(df_all_filt[df_all_filt.總樓層數=="十一層"].index)
df_all_filt=df_all_filt.drop(df_all_filt[df_all_filt.總樓層數=="十二層"].index)
df_all_filt.to_csv('filter_a.csv')
print(len(df_all_filt))



df_all['總車位數']=df_all['交易筆棟數'].map(lambda x:x. split('車位')[1]).astype(int)
df_all['平均車位總價元']=df_all['車位總價元'].astype(int)/df_all['總車位數']

print(df_all['平均車位總價元'])


       
    







