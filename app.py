import streamlit as st
from scraper import (
    scrape_economic_times,
    scrape_the_hindu,
    scrape_times_of_india,
    scrape_indian_express,
)

st.set_page_config(page_title="News CSS Extractor", layout="centered")

st.title("📰 News Extractor Using CSS Selectors")

tab1, = st.tabs(["🔍 Extract News"])

with tab1:
    st.subheader("1. Choose a News Site")
    site = st.selectbox(
        "Select site",
        ["The Hindu", "Economic Times", "Times of India", "Indian Express"]
    )

    st.subheader("2. Enter Full Article URL")
    url = st.text_input("Paste the article URL here")

    if st.button("Extract"):
        if not url:
            st.error("Please enter a valid article URL.")
        else:
            with st.spinner("Extracting content..."):
                try:
                    if site == "Economic Times":
                        data = scrape_economic_times(url)
                    elif site == "The Hindu":
                        data = scrape_the_hindu(url)
                    elif site == "Times of India":
                        data = scrape_times_of_india(url)
                    elif site == "Indian Express":
                        data = scrape_indian_express(url)
                    else:
                        data = {"article": "Unknown site", "publisher": "", "date": ""}

                    st.success("✅ Extraction Successful!")
                    st.markdown(f"**🗞 Publisher:** {data['publisher']}")
                    st.markdown(f"**📅 Published Date:** {data['date']}")
                    st.markdown("**🧾 Article Content:**")
                    st.write(data["article"])

                except Exception as e:
                    st.error(f"❌ Error extracting article: {e}")

