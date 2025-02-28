import altair as alt
import numpy as np
import pandas as pd
import streamlit as st


def main():
    st.sidebar.title("My Streamlit App")
    app_selection = st.sidebar.radio("Select an Application:", ["App 1", "App 2", "App 3", "App 4", "App 5"])
    
    st.title(app_selection)
    st.write(f"Welcome to {app_selection}!")
    
if __name__ == "__main__":
    main()


