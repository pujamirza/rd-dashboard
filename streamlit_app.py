import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials

st.set_page_config(page_title="🔍 Sheet Access Diagnostic", layout="wide")
st.title("🧪 Google Sheet Connection Test")

# Setup credentials
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_dict(st.secrets["gcp_service_account"], scope)
client = gspread.authorize(creds)

try:
    # Try to open by key
    sheet = client.open_by_key("1qrXjp8Z_2hGAThsuwE14TCv2sPQsZJMiplomTBeXBog")
    st.success("✅ Successfully connected to the Google Sheet.")

    # List all available worksheet names
    tabs = sheet.worksheets()
    st.write("📄 Sheet Tabs Found:")
    for tab in tabs:
        st.markdown(f"- {tab.title}")

except Exception as e:
    st.error(f"❌ Failed to connect to the sheet.\n\n**Error:** {e}")
