"""Configuration for local model settings."""
from enum import Enum
from dataclasses import dataclass
from typing import Optional, Dict, Any

class ModelType(Enum):
    LLAMA2 = "llama2"
    MISTRAL = "mistral"
    GPT4ALL = "gpt4all"

@dataclass
class ModelConfig:
    model_type: ModelType
    model_path: str
    context_length: int
    temperature: float = 0.7
    top_p: float = 0.95
    repeat_penalty: float = 1.1

# Default configurations for local models
DEFAULT_CONFIGS = {
    ModelType.LLAMA2: ModelConfig(
        model_type=ModelType.LLAMA2,
        model_path="models/llama-2-7b-chat.gguf",  # Default path, should be configured
        context_length=4096,
        temperature=0.7,
        top_p=0.95,
        repeat_penalty=1.1
    ),
    ModelType.MISTRAL: ModelConfig(
        model_type=ModelType.MISTRAL,
        model_path="models/mistral-7b-instruct-v0.1.Q4_K_M.gguf",
        context_length=8192,
        temperature=0.7,
        top_p=0.95,
        repeat_penalty=1.1
    ),
    ModelType.GPT4ALL: ModelConfig(
        model_type=ModelType.GPT4ALL,
        model_path="models/gpt4all-13b-snoozy.gguf",
        context_length=2048,
        temperature=0.7,
        top_p=0.95,
        repeat_penalty=1.1
    )
}

def get_recommended_model() -> ModelConfig:
    """Get the recommended model configuration for the current system."""
    # For macOS, Llama 2 is recommended for its balance of performance and capabilities
    return DEFAULT_CONFIGS[ModelType.LLAMA2]

def get_model_config(model_type: ModelType) -> ModelConfig:
    """Get configuration for a specific model type."""
    return DEFAULT_CONFIGS[model_type]
