# RepoParser 🤖

> **Chat with your GitHub Repositories using RAG & AST Parsing.**

RepoParser is an AI-powered tool that allows you to ingest any GitHub repository and ask questions about its codebase. It uses **Abstract Syntax Tree (AST)** parsing to split code intelligently (preserving classes and functions) and **Pinecone** for vector storage.

## 🌟 Features

- **Smart Ingestion**: Clones public GitHub repositories and parses Python files.
- **AST-Aware Splitting**: Uses `RecursiveCharacterTextSplitter.from_language` to respect code structure (classes, functions) rather than naive text splitting.
- **Vector Search**: Embeds code chunks using OpenAI and stores them in a Pinecone Serverless Index.
- **RAG Architecture**: Retrieves the most relevant code snippets ($\text{k}=20$) to answer user queries accurately.
- **Fresh Context**: Automatically wipes the index between sessions to ensure no "memory pollution" from previous repos.
- **Interactive UI**: Built with Streamlit for a clean, chat-like experience.

## 🛠️ Tech Stack

- **Frontend**: Streamlit
- **LLM**: OpenAI GPT-4o-mini
- **Vector Database**: Pinecone (Serverless)
- **Framework**: LangChain (LCEL)
- **Parsing**: `gitpython`, `langchain-text-splitters`

## 🚀 Setup & Installation

1.  **Clone the Repository**
    ```bash
    git clone https://github.com/your-username/RepoParser.git
    cd RepoParser
    ```

2.  **Create a Virtual Environment**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install Dependencies**
    ```bash
    pip install -r RepoChat/requirements.txt
    ```

4.  **Configure Environment Variables**
    Create a `.env` file in the `RepoChat` directory:
    ```bash
    # RepoChat/.env
    OPENAI_API_KEY=sk-...
    PINECONE_API_KEY=pcsk_...
    ```

## 🏃 Usage

1.  **Run the App**
    ```bash
    cd RepoChat
    streamlit run app.py
    ```

2.  **Analyze a Repo**
    - Paste a GitHub URL (e.g., `https://github.com/hwchase17/langchain`) in the sidebar.
    - Click **"Analyze Codebase"**.
    - Wait for the "✅ Repository Indexed!" message.

3.  **Chat**
    - Ask questions like "How is the `PythonLoader` class implemented?" or "Where is the retry logic?".

## 📂 Project Structure

```
RepoChat/
├── src/
│   ├── ingestion.py       # Cloning & AST Parsing logic
│   ├── vector_store.py    # Pinecone Index management
│   ├── rag_chain.py       # RAG Chain implementation (LCEL)
│   └── utils.py           # Helper utilities
├── app.py                 # Main Streamlit application
└── requirements.txt       # Dependencies
```
