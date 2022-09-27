# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 14:23:08 2021
Routine to plot Felicia's multiple-drifter-type tracks

@author: James.manning
"""
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
df=pd.read_csv('2019_DrifterData_GoodClusters.csv') # makes a dataframe
df['datetime']=pd.to_datetime(df['Date']+' '+df['Time']) # forms a "datetime" variable (not needed yet) from the two columns
jc=0
colors=['r','g','b','m'] # colors to distinguish types
linetype=['-',':','--']    
for j in np.unique(df['Type'].dropna()): # loop through unique types
        dft=df[df['Type']==j]# just this type
        jd=0
        for i in np.unique(dft['Deployment ID']): # loop through unique deployments
            dfid=dft[dft['Deployment ID']==i] # just this deployment id
            plt.plot(dfid['Longitude'],dfid['Latitude'],linestyle=linetype[jd],label=j+' '+dfid['datetime'].values[0].astype(str)[5:10],color=colors[jc])# colors by type
            jd=jd+1
        jc=jc+1
plt.legend()
plt.savefig('plot_multitype_tracks.png')