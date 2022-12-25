import streamlit as st
import pandas as pd


st.title('Locations of Agriculural Fire 🔥 in Telangana')

#@st.cache(persist=True)
df = pd.read_csv('task_ff.csv')
df = df.drop(['Unnamed: 0'],axis=1)

v = df[df['cluster']==2]
l1 = list(v['District'].value_counts().index)
l2 = []
l3 = []
for i in l1:
  l2.append((v[v['District']==i][['latitude']]).mean()[0])
  l3.append((v[v['District']==i][['longitude']]).mean()[0])


vv = pd.DataFrame(data=l1,columns=['District'])
vv['latitude'] = pd.DataFrame(l2)
vv['longitude'] = pd.DataFrame(l3)
vv['No_of_fire_events'] = pd.DataFrame(v['District'].value_counts().values)

st.header('Which District has the most number of Agricultural Fire')
agri_fire_events = st.slider('No. of Agricultural fires in Telangana',2,534)
st.map(vv.query('No_of_fire_events >= @agri_fire_events')[['latitude','longitude']])

if st.checkbox('Show raw data',False):
    st.subheader('Raw Data')
    st.write(vv)



