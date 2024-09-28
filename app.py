import streamlit as st



def main():
    st.set_page_config(page_title="Chat with PDFs")
    st.header("Chat with PDFs")
    st.text_input("Ask a question")
    
    with st.sidebar:
        st.subheader("Your Documents")
        st.file_uploader("Upload Your PDF")
        st.button("Process")

if __name__ == '__main__':
    main()