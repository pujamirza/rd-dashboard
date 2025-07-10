import streamlit as st
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials

st.set_page_config(page_title="R&D Projects Dashboard", layout="wide")
st.title("📊 R&D Projects Overview")

# Setup connection
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_dict(st.secrets["gcp_service_account"], scope)
client = gspread.authorize(creds)

# Open your Google Sheet
sheet = client.open_by_key("1xThS4taeMU-1J0PpkT8x6eg4tHdgiqJf1-201Bz18394A4g")


# Load a specific worksheet
projects_data = sheet.worksheet("ProjectsList").get_all_records()
projects_df = pd.DataFrame(projects_data)

# Display data
st.dataframe(projects_df)
