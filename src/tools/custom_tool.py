from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
import requests
import os

class SerperInput(BaseModel):
    query: str = Field(..., description="The search query string.")

class SerperTool(BaseTool):
    name: str = "Serper Search Tool"
    description: str = "Search the web using Serper.dev API to gather competitor, pricing, and market insights."
    args_schema: Type[BaseModel] = SerperInput

    def _run(self, query: str) -> str:
        url = "https://google.serper.dev/search"
        headers = {"X-API-KEY": os.getenv("SERPER_API_KEY"), "Content-Type": "application/json"}
        payload = {"q": query}

        response = requests.post(url, headers=headers, json=payload)
        if response.status_code == 200:
            results = response.json()
            return str(results)
        else:
            return f"Serper API error: {response.status_code} - {response.text}"