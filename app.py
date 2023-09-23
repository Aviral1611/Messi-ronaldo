import pandas as pd
import plotly_express as px
import streamlit as st

st.set_page_config(page_title="Football",page_icon=":wave:",layout="wide")



df = pd.read_excel(
    io='MessiRonaldo.xlsx',
   
)




st.header("A Analysis of Messi and Ronaldo's Season till their time in LA LIGA including the champions league stats!")





st.sidebar.header("Please filter here:")
player = st.sidebar.multiselect(
    "Select the player:",
    options=df["Player"].unique(),
    default=df["Player"].unique()
)

season = st.sidebar.multiselect(
    "Select the season:",
    options=df["Season"].unique(),
    default=df["Season"].unique()
)

df_selection = df.query(
    "Player == @player & Season == @season"
    
)

st.dataframe(df_selection)


st.title(":bar_chart: Football Dashboard")
st.markdown("##")

total_ll_goals = int(df_selection["Liga_Goals"].sum())
total_cl_goals = int(df_selection["CL_Goals"].sum())
total_ll_asis = int(df_selection["Liga_Asts"].sum())
total_cl_asis = int(df_selection["CL_Asts"].sum())

left_column, middle_column , right_column, right1_column = st.columns(4)
with left_column:
    st.subheader("Total la liga Goals")
    st.subheader(f"Goals: {total_ll_goals:,}")

with middle_column:
    st.subheader("Total Champions League Goals")
    st.subheader(f"Goals: {total_cl_goals:,}")

with right_column:
    st.subheader("Total Champions league assists")
    st.subheader(f"Goals:{total_cl_asis:,}")

with right1_column:
    st.subheader("Total la liga assists")
    st.subheader(f"Goals:{total_ll_asis:,}")

st.markdown("---")


hide_st_style = """
<style>
  #MainMenu {visibility: hidden;}
  footer {visibility: hidden;}
  
  
  </style>
"""
st.markdown(hide_st_style,unsafe_allow_html=True)

'''


    [![Repo](https://badgen.net/badge/icon/GitHub?icon=github&label)](https://github.com/Aviral1611?tab=repositories) 

'''
st.markdown("<br>",unsafe_allow_html=True)







