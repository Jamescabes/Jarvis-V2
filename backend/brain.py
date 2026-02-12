from .memory import memory
import time

class JarvisBrain:
    """
    The 'Brain' coordinates memory and LLM processing.
    """
    def __init__(self):
        self.personality = "Formal, elegant, and protective. Like a mix of Jarvis and Alfred."

    async def process_query(self, query: str, user_id: int):
        # 1. Search semantic memory for context
        relevant_memories = memory.query_memory(query)
        context = ""
        if relevant_memories['documents']:
            context = "\n".join(relevant_memories['documents'][0])
        
        # 2. Store the current query as a new memory
        memory.store_memory(query, {"user_id": user_id, "timestamp": time.time()})
        
        # 3. Simulate LLM response (to be replaced by real LLM call)
        response = f"Señor, he registrado su consulta: '{query}'. "
        if context:
            response += "Basado en mis datos previos, esto parece relevante..."
        
        return response

brain = JarvisBrain()
