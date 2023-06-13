import streamlit as st
from datetime import datetime

start = st.date_input(
    "What date are you departing",
    datetime.date(2023, 6, 12)
)

end = st.date_input(
    "What date are you returning",
    datetime.date(start)
)

origin = st.text_input('Where are you departing from?', '')

destination = st.text_input('Where are you flying to?', '')

travelers = st.number_input('How many people will be traveling?')