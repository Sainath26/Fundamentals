import streamlit as st
import pandas as pd
import sqlalchemy


st.title('Fundamental Analysis')

engine = sqlalchemy.create_engine('sqlite:///Fundamentals.db')

df = pd.read_sql('Fundamentalstable',
                engine,index_col=['symbol'])


dropdownI = st.selectbox('choose the sector',
                        df.sector.unique())

dropdownII = st.selectbox('choose your metric',
                          df.columns[df.columns != 'sector'])



values = df[df.sector==dropdownI][[dropdownII]]

st.bar_chart(values)