import os
from pathlib import Path

from dotenv import load_dotenv

env_path = Path('.') / '.env.dev'
print(f"Loading .env file from: {env_path}")  # Debugging
load_dotenv(dotenv_path=env_path)

print(f"API_PREFIX from .env: {os.getenv('API_PREFIX')}")  # Debugging
class Config():

    

    POSTGRES_USER : str = os.getenv("POSTGRES_USER","postgres")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD","BGFTN@1234")
    POSTGRES_SERVER : str = os.getenv("POSTGRES_SERVER", "db")
    POSTGRES_PORT : int = int(os.getenv("POSTGRES_PORT", 5432)) # default postgres port is 5432
    POSTGRES_DB : str = os.getenv("POSTGRES_DB","experiments")
    POSTGRES_SCHEMA: str = os.getenv("POSTGRES_SCHEMA", "public")
    DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"

    BASE_URL = os.getenv("BASE_URL", "http://localhost:8000")
config = Config()