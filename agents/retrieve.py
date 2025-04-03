from utility.retriever import get_retriever

retriever = get_retriever()
def retrieve(state):
    """
    Retrieve documents

    Args:
        state (dict): The current graph state

    Returns:
    
    """
    print("---RETRIEVE---")
    
    question = state["question"]
    
    documents = retriever.get_relevant_documents(question)
    
    return {"documents": documents, "question": question}

if __name__ == "__main__":
    print(retrieve({"question": "what is attention?"}))