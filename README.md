# VisualRagQA

# RAG-Based Question Answering System

This repository contains a **Retrieval-Augmented Generation (RAG) system** for answering user queries based on document retrieval and external search.

## Features
- Retrieves relevant documents based on the user's question.
- Grades retrieved documents for relevance.
- Transforms the query if no relevant documents are found.
- Performs a web search if needed.
- Generates an answer using a language model.

## Installation
### Prerequisites
Ensure you have **Python 3.8+** installed.

### Clone the Repository
```bash
git clone https://github.com/your-repo/rag-question-answering.git
cd rag-question-answering
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

## Usage
Run the main script to start the RAG workflow:
```bash
python main.py
```

## Workflow
The system follows this flow:
1. **Retrieve**: Fetch relevant documents from a vector database.
2. **Grade Documents**: Assess document relevance.
3. **Decide Next Step**:
   - If documents are relevant → Proceed to generation.
   - If no relevant documents → Transform query.
4. **Transform Query**: Modify query for better search.
5. **Web Search**: Search external sources if needed.
6. **Generate Answer**: Generate a response using an LLM.

## Code Structure
```plaintext
📂 rag-question-answering/
├── agents/                   # Contains agent functions for each step
│   ├── generate.py           # Answer generation module
│   ├── retrieve.py           # Document retrieval module
│   ├── transform_query.py    # Query transformation logic
│   ├── web_search.py         # External web search
│   ├── grade_documents.py    # Document grading logic
│   ├── decide_to_generate.py # Decision logic for next steps
├── utility/
│   ├── retriever.py          # Vector store management
├── docs/                     # Documentation and guides
│   ├── document.pdf          # System architecture details
├── main.py                   # Entry point for running the workflow
├── requirements.txt          # Dependencies
└── README.md                 # Project overview and instructions

```

## Example
When prompted, enter a question:
```bash
Enter your question: What is machine learning?
```
The system will retrieve relevant documents, perform query transformations if needed, and generate an answer.

## Contributing
Pull requests are welcome. If you find a bug or want to suggest improvements, open an issue.

## License
This project is licensed under the MIT License.

