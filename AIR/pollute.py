import pandas as pd
df=pd.read_csv("./andhra.csv",parse_dates=["Sampling Date"])
df.head()


# In[5]:


df.describe()


# In[6]:


df=df.drop(['PM 2.5'],axis=1)


# In[7]:


df.columns


# In[8]:


df=df.drop(['Stn Code','State','Type of Location','Agency',],axis=1)


# In[9]:


df.drop(['Location of Monitoring Station'],axis=1,inplace=True)


# In[10]:


df.describe()


# In[11]:


df.rename(columns={'RSPM/PM10': 'PM10', 'City/Town/Village/Area': 'Place'}, inplace=True)


# In[12]:


df.columns


# In[13]:


df.rename(columns={'Sampling Date': 'Date'}, inplace=True)


# In[14]:


df.dropna(inplace=True)


# In[15]:


df.describe()


# In[16]:


df.dtypes


# In[17]:


w = df["Place"].unique()


# In[18]:


print(sorted(w))


# In[19]:


df.columns


# In[20]:


df["Place"].value_counts()


# In[21]:


# Performing One hot Label encoding

pd.get_dummies(df, columns=["Place"]).head()


# In[22]:


df.dtypes


# In[23]:


df1=df


# In[24]:


df1["Place"] = df1["Place"].astype('category')


# In[25]:


df1.dtypes


# In[26]:


df1["Place"] = df1["Place"].cat.codes

df1.head()


# In[28]:


df1.groupby(df1["Place"])['PM10'].sum()


# In[29]:


df3=df1.groupby([df1['Date'].dt.strftime('%B'),df1["Place"]])['PM10','SO2','NO2'].mean()


# In[30]:


df3.index


# In[31]:


df4=df.groupby([df['Date'].dt.strftime('%B'),df["Place"]])['PM10','NO2','SO2'].median()


# In[32]:


df4=df4.reset_index()


# In[33]:


df4=pd.get_dummies(df4, columns=["Place"])


# In[34]:


df5=pd.get_dummies(df4, columns=["Date"])


# In[35]:


df5.columns


# In[36]:


df5.head()


# In[37]:


#create a dataframe with all training data except the target column
train_X = df5.drop(columns=['PM10','SO2','NO2'])
#train_X = df5.drop(columns=['NO2'])
#train_X = df5.drop(columns=['SO2'])

#check that the target variable has been removed
train_X.head(1)


# In[38]:


#create a dataframe with only the target column
train_y = df5[['PM10','SO2','NO2']]

#view dataframe
train_y.head(1)


# In[39]:


from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(train_X, train_y, random_state=42)


# In[40]:


import os
from sklearn.tree import DecisionTreeClassifier, export_graphviz
import pandas as pd
import numpy as np
from time import time
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import SGDRegressor
from sklearn.preprocessing import StandardScaler
from sklearn import metrics
from sklearn.pipeline import Pipeline
from sklearn.metrics import roc_auc_score , classification_report, mean_squared_error, r2_score
from sklearn.metrics import precision_score, recall_score, accuracy_score, classification_report

from sklearn.pipeline import Pipeline
from sklearn.feature_selection import *
from sklearn import metrics


# In[41]:


from sklearn.ensemble import RandomForestRegressor

forest = RandomForestRegressor(n_estimators=1000, 
                               criterion='mse', 
                               random_state=1, 
                               n_jobs=-1)
forest.fit(x_train, y_train)
y_train_pred = forest.predict(x_train)
y_test_pred = forest.predict(x_test)

print('MSE train: %.3f, test: %.3f' % (
        mean_squared_error(y_train, y_train_pred),
        mean_squared_error(y_test, y_test_pred)))
print('R^2 train: %.3f, test: %.3f' % (
        r2_score(y_train, y_train_pred),
        r2_score(y_test, y_test_pred)))


# In[42]:


import numpy as np
test=np.array([[0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0]])
test.shape


# In[43]:


print(x_test.head(1))
print(y_test.head(1))


# In[44]:


res = forest.predict([x_test.loc[19]])


# In[45]:


res = forest.predict(test)


# In[46]:


print(res.round())



np.array([x_test.loc[19]]).shape


from sklearn.externals import joblib
joblib.dump(forest, 'model_air.pkl')
print('Model dumped')

lr = joblib.load('model_air.pkl')



    