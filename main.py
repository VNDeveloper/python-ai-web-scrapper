import streamlit as st
from scrape import scrape_website, split_dom_content, clean_body_content, extract_body_content

st.title("AI Web Scraper")
url = st.text_input("Enter the URL to scrape:")

if st.button("Scrape"):
  if url:
      st.write(f"Scraping data from: {url}")
      # Here you would add the logic to scrape the URL
      # For example, using requests and BeautifulSoup
      # But for now, we will just simulate a response
      st.write("Data scraped successfully!")
      result = scrape_website(url)

      body_content = extract_body_content(result)
      cleaned_content = clean_body_content(body_content)

      st.session_state.dom_content = cleaned_content

      with st.expander("View DOM Content"):
        st.text_area("DOM Content", cleaned_content, height=300)
  else:
      st.error("Please enter a valid URL.")

if "dom_content" in st.session_state:
   parse_description = st.text_area("Describe what you want to parse?")

   if st.button("Parse Content"):
      if parse_description:
        st.write("Parsing the content")

        dom_chunks = split_dom_content(st.session_state.dom_content)