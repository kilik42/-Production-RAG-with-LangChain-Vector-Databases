import os
import tempfile
from pathlib import Path
from langchain_community.document_loaders import TextLoader, PyPDFLoader, UnstructuredPDFLoader, TextLoader, CSVLoader
from langchain_core import Document

from dotenv import load_dotenv

load_dotenv()


def load_text_file():
    # Create a temporary text file for demonstration
    with tempfile.NamedTemporaryFile(delete=False, suffix=".txt") as temp_file:
        temp_file.write(
            b"Hello, this is a sample text file.\nThis file is used to"
        )
        temp_file_path = temp_file.name

    try:
        # Load the text file using TextLoader
        loader = TextLoader(temp_file_path)
        documents = loader.load()

        # Print the loaded documents
        for doc in documents:
            print(doc.page_content)
    finally:
        # Clean up the temporary file
        os.remove(temp_file_path)

# Run the function
load_text_file()
