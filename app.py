import os
import streamlit as st
import uuid
import psycopg2
from dotenv import load_dotenv

st.set_page_config(page_title="ShareBin", page_icon="📂")
load_dotenv("db.env")

DB_URL = os.getenv("DATABASE_URL")

def connect_db():
    return psycopg2.connect(DB_URL)

def save_data(id, path):
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("INSERT INTO files (code, file_path) VALUES (%s, %s);", (id, path))
    db.commit()
    cursor.close()
    db.close()

def download_file(code):
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("SELECT file_path FROM files WHERE code = %s;", (code,))
    result = cursor.fetchone()
    cursor.close()
    db.close()
    return result[0] if result else None

def main():
    st.title("\U0001F4C2 File Upload & Download")
    uploaded = st.file_uploader("UPLOAD HERE :)")
    
    if uploaded:
        uID = uuid.uuid4().hex[:8]
        file_dir = os.path.join(os.getcwd(), "files")
        os.makedirs(file_dir, exist_ok=True)
        filepath = os.path.join(file_dir, f"{uID}_{uploaded.name}")
        
        with open(filepath, 'wb') as f:
            f.write(uploaded.getbuffer())
        
        save_data(uID, filepath)
        st.success(f"\u2705 Your unique code: `{uID}` (Use this to download your file)")
    
    st.header("\U0001F511 Enter Code to Download File")
    textIn = st.text_input("Unique Code")
    
    if textIn:
        st.info(f"The entered unique code is: `{textIn}`")
        file_path = download_file(textIn)
        
        if file_path:
            with open(file_path, "rb") as file:
                st.download_button(label="\U0001F4E5 Download File", data=file, file_name=os.path.basename(file_path))
        else:
            st.error("❌ Invalid Code! No file found.")

if __name__ == "__main__":
    main()
