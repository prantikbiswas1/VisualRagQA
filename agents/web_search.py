from langchain.schema import Document
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper

# Initialize Wikipedia tool
web_search_tool = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper(top_k_results=3))

def web_search(state):
    """
    Wikipedia search based on the re-phrased question.

    Args:
        state (dict): The current graph state
            - "question": str
            - "documents": list[Document]

    Returns:
        state (dict): Updated state with appended Wikipedia results
    """
    print("---WIKIPEDIA SEARCH---")
    question = state["question"]
    documents = state["documents"]

    # Wikipedia search
    wiki_content = web_search_tool.run(question)
    
    # Create a single document with all results
    web_results = Document(
        page_content=wiki_content,
        metadata={"source": "wikipedia"}
    )
    
    documents.append(web_results)

    return {"documents": documents, "question": question}