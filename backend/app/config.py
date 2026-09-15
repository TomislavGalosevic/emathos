from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    secret_key: str = "promijeni-me-u-produkciji-nasumicni-tajni-kljuc"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 60 * 24

    database_url: str = "sqlite:///./emathos.db"

    admin_username: str = "admin"
    admin_email: str = "admin@emathos.hr"
    admin_password: str = "admin123"

    class Config:
        env_file = ".env"


settings = Settings()
