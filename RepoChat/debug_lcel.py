try:
    from langchain_core.prompts import ChatPromptTemplate
    from langchain_core.runnables import RunnablePassthrough
    from langchain_core.output_parsers import StrOutputParser
    print("SUCCESS: langchain_core primitives found.")
except ImportError as e:
    print(f"FAILURE: {e}")

try:
    from langchain_openai import ChatOpenAI
    print("SUCCESS: langchain_openai found.")
except ImportError as e:
    print(f"FAILURE: {e}")
