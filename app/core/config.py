from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    # App & Security
    SECRET_KEY: str

    # Database
    DB_URL: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    model_config = SettingsConfigDict(env_file=".env", extra="forbid")  # forbid agar ketat, atau pakai "allow" jika longgar


settings = Settings()
