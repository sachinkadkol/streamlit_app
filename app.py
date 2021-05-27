import streamlit as st

from multipage import MultiPage
import page2,page3
import home

# Create an instance of the app
app = MultiPage()

st.title("Streamlit multiple page application")

app.add_page("Home page", home.app)
app.add_page("Page2", page2.app)
app.add_page("Page3", page3.app)


app.run()
