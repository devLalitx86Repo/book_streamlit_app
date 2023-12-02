import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
from views.barcharts import bar_avgPrice_per_rating
from views.kpis import kpi_visual, show_top_10_books
from views.style import apply_style
from views.filters import show_filter_visual

from snowflake.snowpark import Session

st.set_page_config(
    page_title = 'Book Data Dashboard',
    page_icon = '📘',
    layout = 'wide'
)

apply_style(st)

st.title('🧑‍💻 DE Coding Challenge')

# Establish Snowflake session
@st.cache_resource
def create_session():
    return Session.builder.configs(st.secrets.snowflake).create()

session = create_session()
st.success("Connected to Snowflake!")
  
# Load data table
@st.cache_data
def load_data(table_name):
    ## Read in data table
    st.write(f"Here's some example data from `{table_name}`:")
    table = session.table(table_name)    
    ## Do some computation on it
    table = table.limit(1000)    
    ## Collect the results. This will run the query and download the data
    table = table.collect()
    return table

table_name = "books.public.table_books"
## Display data table
with st.expander("See Table"):
    df = load_data(table_name)
    st.dataframe(df)

# convert to dataframe
df = pd.DataFrame(df)

# Filters
df = show_filter_visual(st,df)

# KPIS
kpi_visual(df)

#add a divider
st.markdown("---")

# Bar Chart 
# 1. Average price per rating
bar_avgPrice_per_rating(st,df)

#add a divider
st.markdown("---")

# Tables
show_top_10_books(st,df)


#Footer

st.markdown("---")
st.markdown("Submitted by: **Lalit Gupta**")









