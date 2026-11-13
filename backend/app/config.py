from pydantic import BaseSettings, Field

class Settings(BaseSettings):
    FASTAPI_HOST: str = Field(default="127.0.0.1", env="FASTAPI_HOST")
    FASTAPI_PORT: int = Field(default=8000, env="FASTAPI_PORT")
    GEMINI_API_KEY: str = Field(default="YOUR_GEMINI_API_KEY", env="GEMINI_API_KEY")
    TESSERACT_CMD: str = Field(default="tesseract", env="TESSERACT_CMD")
    CORS_ORIGINS: str = Field(default="http://localhost:5173", env="CORS_ORIGINS")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
