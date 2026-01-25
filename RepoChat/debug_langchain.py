import langchain
import pkgutil
import sys
import importlib

print(f"LangChain Version: {langchain.__version__}")
print(f"LangChain contents: {dir(langchain)}")

# Check if we can find create_retrieval_chain in obvious places
candidates = [
    "langchain.chains", 
    "langchain.chains.retrieval",
    "langchain.rag", 
    "langchain.retrieval",
    "langchain_core.runnables",
    "langchain_core.chains"
]

for c in candidates:
    try:
        mod = importlib.import_module(c)
        if hasattr(mod, "create_retrieval_chain"):
            print(f"FOUND create_retrieval_chain in {c}")
        else:
            print(f"Checked {c}, but not found therein.")
    except ImportError as e:
        print(f"Could not import {c}: {e}")

# Try to find where create_stuff_documents_chain is
try:
    from langchain.chains.combine_documents import create_stuff_documents_chain
    print("Found create_stuff_documents_chain in langchain.chains.combine_documents")
except ImportError as e:
    print(f"Failed to import create_stuff_documents_chain: {e}")
