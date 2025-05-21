class SimpleChatBot:
    def __init__(self, vectorstore):
        self.retriever = vectorstore.as_retriever(search_kwargs={"k": 2})

    def ask(self, query: str):
        results = self.retriever.invoke(query)
        if not results:
            return "Sorry, I couldn't find any information related to your question."
        
        return "\n\n".join([f"• {doc.page_content}" for doc in results])
