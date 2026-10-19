import os # this is used to set the SSL_CERT_FILE environment variable for conda/python environments
import certifi # this is used to get the path to the certifi certificate bundle
from dotenv import load_dotenv # used to load variable from .env file

# --- AUTOMATIC SSL FIX FOR CONDA/PYTHON ENVIRONMENTS ---
ssl_cert = os.environ.get('SSL_CERT_FILE') # ssl ceritificate is used for secure connections to external services like OpenAI and Pinecone
if ssl_cert and not os.path.exists(ssl_cert): # if the SSL_CERT_FILE environment variable is set but the file does not exist, set it to the certifi certificate bundle
    os.environ['SSL_CERT_FILE'] = certifi.where() # ceritifi.where() returns the path to the certifi certificate bundle
elif not ssl_cert:
    os.environ['SSL_CERT_FILE'] = certifi.where()
# --------------------------------------------------------

load_dotenv()
from pydantic_settings import BaseSettings, SettingsConfigDict # BaseSettings is used to define the settings for the application, SettingsConfigDict is used to configure the settings class



class Settings(BaseSettings):
    groq_api_key: str = ''
    pinecone_api_key: str = ''
    tavily_api_key: str = ''
    gemini_api_key: str = ''
    pinecone_index: str = 'medical-agent-demo'
    groq_chat_model: str = 'openai/gpt-oss-120b'
    gemini_embed_model: str = 'gemini-embedding-2'
    groq_vision_model: str = 'qwen/qwen3.8-27b'
    api_token: str = ''
    allowed_origins: str = 'http://localhost:8000,http://127.0.0.1:8000'
    model_config = SettingsConfigDict(env_file='.env', extra='ignore')


settings = Settings()