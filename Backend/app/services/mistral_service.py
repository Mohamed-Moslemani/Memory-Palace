from mistralai import Mistral
from typing import List, Dict, Any
import os

class MistralService:
    def __init__(self):
        self.client = Mistral(api_key=os.getenv("MISTRAL_API_KEY"))
        self.agent_id = os.getenv("MISTRAL_AGENT_ID")

    def generate_response(self, query: str, context: List[Dict[str, Any]]) -> str:
        # Format context
        formatted_context = self._format_context(context)
        
        try:
            response = self.client.agents.complete(
                agent_id=self.agent_id,
                messages=[
                    {
                        "role": "system",
                        "content": "You are a helpful AI assistant. Use the provided context to answer questions accurately."
                    },
                    {
                        "role": "user",
                        "content": f"User's info:\n{formatted_context}\n\Query: {query}"
                    }
                ]
            )
            return response.choices[0].message.content
        except Exception as e:
            raise Exception(f"Mistral API error: {str(e)}")

    def _format_context(self, context: List[Dict[str, Any]]) -> str:
        formatted_items = []
        for item in context:
            if "idea" in item:
                formatted_items.append(f"- Idea: {item['idea']}")
            elif "service" in item:
                formatted_items.append(f"- Service: {item['service']}")
            elif "content" in item:
                formatted_items.append(f"- {item['content']}")
        return "\n".join(formatted_items)
