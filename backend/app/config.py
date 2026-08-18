from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # U produkciji obavezno postaviti preko environment varijable / .env
    secret_key: str = "promijeni-me-u-produkciji-nasumicni-tajni-kljuc"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 60 * 24  # 1 dan

    database_url: str = "sqlite:///./emathos.db"

    # Podaci za pocetnog admina (seed)
    admin_username: str = "admin"
    admin_email: str = "admin@emathos.hr"
    admin_password: str = "admin123"

    class Config:
        env_file = ".env"


settings = Settings()
