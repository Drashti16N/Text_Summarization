import validators
import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain.chains.summarize import load_summarize_chain
from langchain_community.document_loaders import YoutubeLoader, UnstructuredURLLoader
from langchain.document_loaders import WebBaseLoader
from bs4 import BeautifulSoup
import requests

# Set up the app
st.set_page_config(page_title="Text Summarizer", page_icon="📜")
st.title("📜 Text Summarizer")
st.subheader("Summarize Content from YouTube or Website")

# Sidebar for API Key input
with st.sidebar:
    groq_api_key = st.text_input("Enter Groq API Key", type="password")

# URL input
url = st.text_input("Enter URL (YouTube or Website)")

# Prompt for summarization
prompt_template = """
Provide a summary of the following content in 300 words:
Content: {text}
"""
prompt = PromptTemplate(template=prompt_template, input_variables=["text"])


# Button to trigger summarization
if st.button("Summarize"):
    if not groq_api_key.strip() or not url.strip():
        st.error("Please provide both the API key and a valid URL.")
    elif not validators.url(url):
        st.error("Invalid URL. Please enter a valid YouTube or website URL.")
    else:
        try:
            st.info("Processing... Please wait.")

            response = requests.get(url)
            soup = BeautifulSoup(response.content, "html.parser")
            webpage_text = soup.get_text()

            # Create a Document object for LangChain
            from langchain.docstore.document import Document
            docs = [Document(page_content=webpage_text)]

            llm = ChatGroq(model="llama3-8b-8192", groq_api_key=groq_api_key)
            chain = load_summarize_chain(llm, chain_type="stuff", prompt=prompt)
            summary = chain.run(docs)

            st.success("Summary:")
            st.write(summary)
        except Exception as e:
            st.error(f"An error occurred: {e}")
