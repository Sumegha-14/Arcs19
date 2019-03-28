import requests
from bs4 import BeautifulSoup

def get_details(w):
    r=requests.get("https://en.wikipedia.org/wiki/Air_quality_index")
    c=r.content 
    soup=BeautifulSoup(c,"html.parser")
    print(soup.prettify())


    # In[3]:


    table=soup.find_all("table",{"class":"wikitable"})
    table=table[2]


    # In[4]:


    data=table.find_all("tr")


    # In[5]:


    data=data[1:]


    # In[6]:


    aqi=[]
    category=[]
    health_impl=[]
    recommend=[]


    # In[7]:


    info=[]
    for item in data:
        d={}
        try:
            d["aqi"]=item.find_all("td")[0].text.replace("\n","")
            print(item.find_all("td")[0].text.replace("\n",""))
        except:
            d["aqi"]=None
            print(None)
        try:
            print(item.find_all("td")[1].text.replace("\n",""))
        except:
            print(None)
        try:
            d["category"]=item.find_all("td")[2].text.replace("\n","")
            print(item.find_all("td")[2].text.replace("\n",""))
        except:
            d["category"]=None
            print(None)
        try:
            d["health_implications"]=item.find_all("td")[3].text.replace("\n","")
            print(item.find_all("td")[3].text.replace("\n",""))
        except:
            d["health_implications"]=None
            print(None)
        try:
            d["recommend"]=item.find_all("td")[4].text.replace("\n","")
            print(item.find_all("td")[4].text.replace("\n",""))
        except:
            d["recommend"]=None
            print(None)
        info.append(d)
        print("\n")


    # In[8]:


    category


    # In[9]:


    import pandas as pd


    # In[10]:


    df=pd.DataFrame(info)


    # In[11]:


    df


    # In[26]:


    t = df['aqi'][0].split('-')
    print(t[0][0])
    for i in range (6):
        t = list(df['aqi'][i])
        print(t)


    # In[32]:


    if w<=50:
        t = df['category'][0]+' '+df['health_implications'][0]+df['recommend'][0]
    elif w>=51 and w<=100:
        t = df['category'][1]+' '+df['health_implications'][1]+df['recommend'][1]
    elif w>=101 and w<=151:
        t = df['category'][2]+' '+df['health_implications'][2]+df['recommend'][2]
    elif w>=151 and w<=200:
        t = df['category'][3]+' '+df['health_implications'][3]+df['recommend'][3]
    elif w>=201 and w<=300:
        t = df['category'][4]+' '+df['health_implications'][4]+df['recommend'][4]
    elif w>=301:
        t = df['category'][5]+' '+df['health_implications'][5]+df['recommend'][5]


    # In[35]:


    print(t)
    return t;

