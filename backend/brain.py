from .llm_handler import llm

class JarvisBrain:
    """
    The 'Brain' coordinates memory and LLM processing.
    """
    def __init__(self):
        self.system_prompt = "You are Jarvis, a highly sophisticated and protective personal AI assistant. Your tone is formal, elegant, and efficient. You represent a mix between Iron Man's Jarvis and Batman's Alfred."

    async def process_query(self, query: str, user_id: int):
        # 1. Search semantic memory for context
        relevant_memories = memory.query_memory(query)
        context = ""
        if relevant_memories['documents'] and relevant_memories['documents'][0]:
            context = "\n".join(relevant_memories['documents'][0])
        
        # 2. Store the current query as a new memory
        memory.store_memory(query, {"user_id": user_id, "timestamp": time.time()})
        
        # 3. Generate response using LLM with context
        full_system_prompt = self.system_prompt
        if context:
            full_system_prompt += f"\n\nContexto relevante de memorias pasadas:\n{context}"
        
        response = await llm.generate_response(query, system_prompt=full_system_prompt)
        return response

brain = JarvisBrain()
