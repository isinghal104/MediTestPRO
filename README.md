# MediChat Pro

MediChat Pro is an intelligent medical document assistant built with Streamlit and LangChain. It allows users to upload PDF medical documents, process and index them, and interact with the content using a conversational AI interface.

## Features

- Upload and process multiple PDF medical documents
- Extract and index document text using FAISS
- Chat with your documents using an OpenAI-powered model
- User-friendly Streamlit interface

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/medichatpro.git
   cd medichatpro
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set your API key**
   - Add your OpenAI API key to `app/config.py` as `EURI_API_KEY`.

## Usage

1. **Run the Streamlit app**
   ```bash
   streamlit run main.py
   ```

2. **Upload PDF documents**
   - Use the sidebar to upload one or more PDF files.

3. **Chat with your documents**
   - Enter questions in the chat interface and get intelligent responses based on your uploaded documents.

## Project Structure

```
e:\GenAI\Medichatpro
│
├── app/
│   ├── chat_utils.py
│   ├── config.py
│   ├── pdf_utils.py
│   ├── ui.py
│   └── vectorstore_utils.py
├── main.py
├── requirements.txt
└── README.md
```

## Dependencies

- streamlit
- fpdf
- pypdf
- faiss-cpu
- langchain
- langchain_community
- sentence-transformers

## License

MIT License

---

**Note:**  
Replace any references to `euriai` with supported packages like `langchain` if you encounter import errors.
