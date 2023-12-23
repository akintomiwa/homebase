# streamlit_app.py
import streamlit as st
import requests

# URL of your FastAPI app
FASTAPI_URL = "http://127.0.0.1:8000"  # Update with your FastAPI app URL

def fetch_website_info():
    response = requests.get(f"{FASTAPI_URL}/website_info")
    if response.status_code == 200:
        return response.json()
    else:
        st.error("Failed to fetch website info from FastAPI app.")
        return None

def main():
    st.title("My Personal Website / Projects")

    website_info = fetch_website_info()
    if website_info:
        st.header(website_info["name"])
        st.write(website_info["bio"])

        st.subheader("Projects:")
        for project in website_info["projects"]:
            st.write(f"**{project['name']}**: {project['description']}")

if __name__ == "__main__":
    main()
