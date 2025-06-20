# AI Integration Guide

This document provides guidance on integrating AI capabilities into your API application.

## Overview

The template includes support for AI integrations through:

1. **Prompt Templates**: Stored in the `prompts/` directory
2. **AI Service Clients**: Integration with AI providers
3. **Vector Database Support**: For semantic search

## Prompt Templates

Prompt templates are stored in the `prompts/` directory. They can be used to:

- Maintain consistent AI interactions
- Version control your prompts
- Support multiple AI providers

### Example Usage

```python
import os

def load_prompt(name: str, **kwargs) -> str:
    """Load a prompt template and format it with the provided variables."""
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    prompt_path = os.path.join(base_dir, "prompts", f"{name}.txt")
    
    with open(prompt_path, "r") as f:
        prompt_template = f.read()
    
    return prompt_template.format(**kwargs)
```

## AI Service Integration

Create AI service clients in the `services/` directory to interact with AI providers.

### Example OpenAI Integration

```python
import openai
from typing import Dict, List, Optional, Any

from application.params import get_settings


settings = get_settings()


class OpenAIService:
    """Service for interacting with OpenAI APIs."""
    
    def __init__(self):
        openai.api_key = settings.openai_api_key
    
    async def generate_completion(
        self,
        prompt: str,
        model: str = "gpt-4",
        max_tokens: int = 1000,
        temperature: float = 0.7,
    ) -> str:
        """Generate a text completion using OpenAI's API."""
        response = await openai.ChatCompletion.acreate(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=max_tokens,
            temperature=temperature,
        )
        return response.choices[0].message.content
    
    async def generate_embeddings(
        self,
        texts: List[str],
        model: str = "text-embedding-ada-002",
    ) -> List[List[float]]:
        """Generate embeddings for a list of texts."""
        response = await openai.Embedding.acreate(
            model=model,
            input=texts,
        )
        return [item.embedding for item in response.data]
```

## Vector Database Integration

For semantic search and similarity matching, you can integrate with vector databases.

### Example Pinecone Integration

```python
import pinecone
from typing import Dict, List, Optional, Any

from application.params import get_settings


settings = get_settings()


class PineconeService:
    """Service for interacting with Pinecone vector database."""
    
    def __init__(self):
        pinecone.init(
            api_key=settings.pinecone_api_key,
            environment=settings.pinecone_environment,
        )
        self.index = pinecone.Index(settings.pinecone_index_name)
    
    async def upsert_vectors(
        self,
        vectors: List[Dict[str, Any]],
    ) -> Dict[str, Any]:
        """Upsert vectors to the Pinecone index."""
        return self.index.upsert(vectors=vectors)
    
    async def query_vectors(
        self,
        vector: List[float],
        top_k: int = 5,
        filter: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Query vectors from the Pinecone index."""
        return self.index.query(
            vector=vector,
            top_k=top_k,
            filter=filter,
            include_metadata=True,
        )
```

## Putting It All Together

Here's an example of how to use these components together in a route handler:

```python
from fastapi import APIRouter, Depends, HTTPException

from services.openai_service import OpenAIService
from services.pinecone_service import PineconeService


router = APIRouter(tags=["ai"])


def get_openai_service():
    return OpenAIService()


def get_pinecone_service():
    return PineconeService()


@router.post("/search")
async def semantic_search(
    query: str,
    openai: OpenAIService = Depends(get_openai_service),
    pinecone: PineconeService = Depends(get_pinecone_service),
):
    """Perform a semantic search using the query text."""
    # Generate embeddings for the query
    embeddings = await openai.generate_embeddings([query])
    
    # Search for similar vectors
    results = await pinecone.query_vectors(
        vector=embeddings[0],
        top_k=5,
    )
    
    return {"results": results.matches}
```

## Performance Considerations

1. **Caching**: Implement caching for AI responses to reduce costs and latency
2. **Batching**: Batch requests to AI services when possible
3. **Streaming**: Use streaming responses for long-running AI tasks
4. **Fallbacks**: Implement fallback mechanisms for when AI services are unavailable

## Security Considerations

1. **API Key Management**: Store AI service API keys securely
2. **Content Filtering**: Implement content filtering for user inputs
3. **Rate Limiting**: Implement rate limiting to prevent abuse
4. **Monitoring**: Monitor AI service usage and costs