"""This is the main module to run the app"""

# Importing the necessary Python modules.
import streamlit as st

# Import necessary functions from model
from model import load_data

# Import pages
from Tabs import home, data, predict, visualise,about

# Configure the app
st.set_page_config(
    page_title = 'Traffic prediction',
    page_icon = 'random',
    layout = 'wide',
    initial_sidebar_state = 'auto'
)

# Dictionary for pages
Tabs = {
    "***Home***": home,
    "***Data Info***": data,
    "***Visualisation***": visualise,
    "***Prediction***": predict,
    "***About Us***": about
}

# Create a sidebar
# Add title to sidear
st.sidebar.header("Menu",divider='rainbow')

# Create radio option to select the page
page = st.sidebar.radio("Pages", list(Tabs.keys()))

# Loading the dataset.
df, X, y,data1= load_data()

# Call the app funciton of selected page to run
if page in ["***Prediction***", "***Visualisation***"]:
    Tabs[page].app(df, X, y,data1)
elif (page == "***Data Info***"):
    Tabs[page].app(df)
else:
    Tabs[page].app()


