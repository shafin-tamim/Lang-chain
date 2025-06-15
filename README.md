# PDF Chatbot using LangChain and Open LLM

A chatbot that can read PDF documents and answer questions using LangChain and Llama-2 model.

## Prerequisites
- Python 3.8+
- Hugging Face account and access token
- GPU recommended for better performance

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd langchain
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Setup

1. Login to Hugging Face:
```python
from huggingface_hub import login
login()  # Enter your Hugging Face token when prompted
```

2. Prepare your PDF file:
- Place your PDF file in the desired location
- Update the PDF path in the code:
```python
pdf = "path/to/your/pdf/file.pdf"
```

## Usage

1. Run the Jupyter notebook `Pdf_chat-bot_using _open_LLm.ipynb`
2. The notebook will:
   - Load and process the PDF
   - Create embeddings
   - Initialize the LLM model
   - Set up the question-answering chain

3. Ask questions about your PDF:
```python
question = "your question here"
answer = chain.run(question)
print(answer)
```

## Model Information

This project uses:
- Llama-2-7b-chat model for text generation
- sentence-transformers/all-MiniLM-L6-v2 for embeddings
- ChromaDB for vector storage

## Note
Make sure you have enough system resources as the LLM model requires significant memory to run.
