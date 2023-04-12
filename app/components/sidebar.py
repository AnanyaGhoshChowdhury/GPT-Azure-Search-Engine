import streamlit as st
import os


def sidebar():
    with st.sidebar:
        st.image("https://fossbytes.com/wp-content/uploads/2019/07/open-AI-microsoft.jpg")

        st.markdown("---")
        st.markdown("# About")
        st.markdown("""
            GPT Smart Search allows you to ask questions about your
            documents and get accurate answers with instant citations.
            
            This engine finds information from CSA-DA Wiki document base [Wiki](https://dev.azure.com/csadevadvocates/Documentation/_wiki/wikis/Documentation.wiki/15/Welcome)
            
            [Github Repo](https://github.com/parthshiras/GPT-Azure-Search-Engine/)
        """
        )
        st.markdown("---")
