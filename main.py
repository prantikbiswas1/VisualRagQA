from langgraph.graph import END, StateGraph, START
from typing import List
from typing_extensions import TypedDict
from agents import generate, retrieve, transform_query, web_search, grade_documents, decide_to_generate

# Define state
class State(TypedDict):
    question: str
    generation: str
    web_search: str
    documents: List[str]

# Initialize workflow
workflow = StateGraph(State)

# Define nodes
workflow.add_node("retrieve", retrieve)
workflow.add_node("grade_documents", grade_documents)
workflow.add_node("generate", generate)
workflow.add_node("transform_query", transform_query)
workflow.add_node("web_search_node", web_search)

# Define edges
workflow.add_edge(START, "retrieve")
workflow.add_edge("retrieve", "grade_documents")
workflow.add_conditional_edges("grade_documents", decide_to_generate, 
    {"transform_query": "transform_query", "generate": "generate"})
workflow.add_edge("transform_query", "web_search_node")
workflow.add_edge("web_search_node", "generate")
workflow.add_edge("generate", END)

# Compile the app
app = workflow.compile()

DOCS_FOLDER = "./docs"

question = input("Enter your question: ")

result = app.invoke({"question":question})
print(result)