import pandas as pd
import streamlit as st

data = {
    "srNo":[1,2,3,4,5],
    "Gender":["M","F","F","M","M"],
    "Weight": [50,55,60,70,75],
    "Height":[5.5,5.7,5.8,5.9,6.2]
}

df = pd.DataFrame(data)
st.table(df)

# st.scatter_chart(df['weight'],df['height'])

st.line_chart(df)