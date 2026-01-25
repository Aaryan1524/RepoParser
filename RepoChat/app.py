import streamlit as st
import os
import tempfile
from src.ingestion import ingest_repo, clone_repository
from src.vector_store import get_vector_store
from src.rag_chain import get_rag_chain

# Page Config
st.set_page_config(page_title="RepoParser", page_icon="🤖")
st.title("🤖 RepoParser")

# Initialize Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []

# Sidebar for Configuration
with st.sidebar:
    st.header("Repository Setup")
    repo_url = st.text_input("GitHub Repo URL", placeholder="https://github.com/owner/repo")
    
    if st.button("Analyze Codebase"):
        if repo_url:
            with st.spinner("Cloning and Parsing Repository... (This might take a minute)"):
                try:
                    # 0. Clear previous index
                    from src.vector_store import clear_index
                    with st.spinner("Cleaning up old database..."):
                        clear_index()

                    # 1. Clone & Ingest
                    local_path = clone_repository(repo_url)
                    chunks = ingest_repo(local_path)
                    
                    # 2. Vectorize
                    st.info(f"Found {len(chunks)} code chunks. Indexing...")
                    get_vector_store(chunks)
                    
                    st.success("✅ Repository Indexed! You can now chat.")
                except Exception as e:
                    st.error(f"Error: {e}")
        else:
            st.warning("Please enter a valid URL.")

# Chat Interface
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User Input
if prompt := st.chat_input("Ask a question about the code..."):
    # Display user message
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Generate Response
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        
        try:
            # Initialize Chain
            rag_chain = get_rag_chain()
            
            # Get Answer
            response = rag_chain.invoke({"input": prompt})
            answer = response["answer"]
            
            # Format Sources
            sources = list(set([doc.metadata['source'] for doc in response['context']]))
            formatted_sources = "\n\n**Sources:**\n" + "\n".join([f"- `{s}`" for s in sources])
            
            full_response = answer + formatted_sources
            
            message_placeholder.markdown(full_response)
            st.session_state.messages.append({"role": "assistant", "content": full_response})
            
        except Exception as e:
            st.error(f"An error occurred: {e}")