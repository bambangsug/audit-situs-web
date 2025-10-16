import streamlit as st
import requests

def cek_keamanan_situs(url):
    API_KEY = "AIzaSyBNSabQvCo_LNtdxb_ccC8h3qMW-n6GXrU"
    endpoint = f"https://safebrowsing.googleapis.com/v4/threatMatches:find?key={API_KEY}"
    
    payload = {
        "client": {
            "clientId": "netlab-akademik",
            "clientVersion": "1.0"
        },
        "threatInfo": {
            "threatTypes": ["MALWARE", "SOCIAL_ENGINEERING"],
            "platformTypes": ["ANY_PLATFORM"],
            "threatEntryTypes": ["URL"],
            "threatEntries": [{"url": url}]
        }
    }
    
    response = requests.post(endpoint, json=payload)
    return response.json()

# Streamlit UI
st.title("🔍 Audit Keamanan Situs Web")
url = st.text_input("Masukkan URL situs (contoh: http://www.uin-suka.ac.id)")

if st.button("Cek Keamanan"):
    if url:
        hasil = cek_keamanan_situs(url)
        if hasil == {}:
            st.success("✅ Situs aman menurut Google Safe Browsing API.")
        else:
            st.error("⚠️ Situs terdeteksi berisiko!")
            st.json(hasil)
    else:
        st.warning("Mohon masukkan URL terlebih dahulu.")

