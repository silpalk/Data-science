# -*- coding: utf-8 -*-
#kmeans clustering for airlines data
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.cluster import	KMeans
# from scipy.spatial.distance import cdist 
# Kmeans on University Data set 
airlines = pd.read_excel(r"C:\Users\Amarnadh Tadi\Desktop\datascience\assign5\EastWestAirlines.xlsx")

airlines.describe()
airlines.columns
airlines.dtypes
airlines1 = airlines.drop(["ID#"], axis = 1)

# Normalization function 
def norm_func(i):
    x = (i - i.min())	/ (i.max() - i.min())
    return (x)

# Normalized data frame (considering the numerical part of data)
df_norm = norm_func(airlines1.iloc[:, 1:])

###### scree plot or elbow curve ############
TWSS = []
k = list(range(2, 9))

for i in k:
    kmeans = KMeans(n_clusters = i)
    kmeans.fit(df_norm)
    TWSS.append(kmeans.inertia_)
TWSS 
%matplotlib inline  
#screeplot 
plt.plot(k, TWSS, 'ro-');plt.xlabel("No_of_Clusters");plt.ylabel("total_within_SS")
# Selecting 5 clusters from the above scree plot which is the optimum number of clusters 
model = KMeans(n_clusters = 5)
model.fit(df_norm)

model.labels_ # getting the labels of clusters assigned to each row 

mb = pd.Series(model.labels_)  # converting numpy array into pandas series object 
clusters=mb.count()
clusters
from collections import Counter
print(Counter(model.labels_))

airlines1['clust'] = mb # creating a  new column and assigning it to new column 

airlines1.head()
df_norm.head()

airlines1 = airlines1.iloc[:,[11,0,1,2,3,4,5,6,7,8,9,10]]
airlines1.head()

airlines1.iloc[:, 1:].groupby(airlines1.clust).mean()
airlines1['clust']
clusters = kmeans_model.labels_.count()
airlines1.to_csv("Kmeans_EWairlines.csv", encoding = "utf-8")

import os
os.getcwd()

## kmeans clustring for crime data


import pandas as pd
import matplotlib.pyplot as plt

from sklearn.cluster import	KMeans
# from scipy.spatial.distance import cdist 
# Kmeans on University Data set 
crime = pd.read_csv(r"C:\Users\Amarnadh Tadi\Desktop\datascience\assign5\crime_data.csv")

crime.describe()
crime.columns

crime1 = crime.drop(['Unnamed: 0'], axis = 1)

# Normalization function 
def norm_func(i):
    x = (i - i.min())	/ (i.max() - i.min())
    return (x)

# Normalized data frame (considering the numerical part of data)
df_norm = norm_func(crime1.iloc[:,:])

###### scree plot or elbow curve ############
TWSS = []
k = list(range(2, 9))

for i in k:
    kmeans = KMeans(n_clusters = i)
    kmeans.fit(df_norm)
    TWSS.append(kmeans.inertia_)
TWSS   
#screeplot 
plt.plot(k, TWSS, 'ro-');plt.xlabel("No_of_Clusters");plt.ylabel("total_within_SS")
# Selecting 5 clusters from the above scree plot which is the optimum number of clusters 
model = KMeans(n_clusters = 5)
model.fit(df_norm)

model.labels_ # getting the labels of clusters assigned to each row 
mb = pd.Series(model.labels_)  # converting numpy array into pandas series object 
from collections import Counter
Counter(mb)
crime1['clust'] = mb # creating a  new column and assigning it to new column 

crime1.head()
df_norm.head()

crime1 = crime1.iloc[:,[4,0,1,2,3]]
crime1.head()

crime1.iloc[:, 1:].groupby(crime1.clust).mean()
from Collection import Counter
Counter(mb)

crime1.to_csv("Kmeans_crimedata.csv", encoding = "utf-8")


###clustring using kmodes for auto insurance data

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from kmodes.kprototypes import KPrototypes
autoinsure =pd.read_csv(r"C:\Users\Amarnadh Tadi\Desktop\datascience\assign5\Autoinsurance.csv")
autoinsure.columns
autoinsure.describe()
autoinsure.head()
## drop customer data
autoinsure.drop(['Effective To Date'],axis=1,inplace=True)
autoinsure.drop(['Vehicle Class','Sales Channel','Policy Type','Policy', 'Renew Offer Type'],axis =1,inplace =True)
autoinsure.dtypes
ainsure_array=autoinsure.values
ainsure_array[:,8]=ainsure_array[:,8].astype(float)

ainsure_array[:,11]=ainsure_array[:,11].astype(float)
ainsure_array[:,12]=ainsure_array[:,12].astype(float)
ainsure_array[:,13]=ainsure_array[:,13].astype(float)
ainsure_array[:,14]=ainsure_array[:,14].astype(float)
ainsure_array[:,15]=ainsure_array[:,15].astype(float)
ainsure_array
##clustring using kprotypes for clustring
kproto=KPrototypes(n_clusters=3,verbose=2)
cluster=kproto.fit_predict(ainsure_array,categorical=[0,1,3,4,5,6,7,9,10,17])
print(kproto.cluster_centroids_)

cluster_dict=[]
for c in cluster:
    cluster_dict.append(c)
    
cluster_dict  
autoinsure['cluster']=cluster_dict  
autoinsure[autoinsure['cluster']==1].head(10)
from collections import Counter
Counter(autoinsure['cluster'])
