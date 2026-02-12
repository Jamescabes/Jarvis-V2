import os
from openai import OpenAI
import httpx
from dotenv import load_dotenv

load_dotenv()

class LLMHandler:
    """
    Handles LLM requests, switching between Online (OpenAI/Claude) and Offline (Local via Ollama).
    """
    def __init__(self):
        self.use_local = False
        self.api_key = os.getenv("OPENAI_API_KEY")
        self.client = OpenAI(api_key=self.api_key) if self.api_key else None
        self.local_url = os.getenv("LOCAL_LLM_URL", "http://localhost:11434/api/generate")

    async def generate_response(self, prompt: str, system_prompt: str = ""):
        """
        Generates a response using the best available model.
        """
        if self.use_local or not self.api_key:
            return await self._generate_local(prompt, system_prompt)
        
        try:
            response = self.client.chat.completions.create(
                model="gpt-4o-mini", # Standard for speed/cost
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": prompt}
                ]
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"[WARNING] Online LLM failed, falling back to local: {e}")
            return await self._generate_local(prompt, system_prompt)

    async def _generate_local(self, prompt: str, system_prompt: str):
        """
        Calls a local LLM via Ollama API.
        """
        try:
            async with httpx.AsyncClient() as client:
                response = await client.post(
                    self.local_url,
                    json={
                        "model": "llama3", # Default suggested model
                        "prompt": f"{system_prompt}\n\nUser: {prompt}\nJarvis:",
                        "stream": False
                    },
                    timeout=30.0
                )
                if response.status_code == 200:
                    return response.json().get("response", "Señor, el modelo local no devolvió una respuesta válida.")
                else:
                    return "Señor, no puedo establecer conexión con el motor local en este momento."
        except Exception as e:
            return f"Señor, estoy operando en modo de emergencia. No hay IA disponible: {str(e)}"

llm = LLMHandler()
