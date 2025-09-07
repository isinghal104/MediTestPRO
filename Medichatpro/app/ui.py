import streamlit as st

def pdf_uploader():
    uploaded_files = st.file_uploader(
        "Upload PDF files",
        type=["pdf"],
        accept_multiple_files=True,
        help="Upload one or more PDF files to process."
    )
    return uploaded_files