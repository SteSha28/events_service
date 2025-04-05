from pydantic_settings import BaseSettings
import os


class Settings(BaseSettings):
    DB_HOST: str = "localhost"
    DB_PORT: str = "5432"
    DB_USER: str = "postgres"
    DB_PASS: str = "postgres"
    DB_NAME: str = "postgres"

    @property
    def ASYNC_DATABASE_URL(self):
        return (
            f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}"
            f"@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        )

    class Config:
        env_file = ".env"
        if not os.path.exists(env_file):
            print(f"Файл .env не найден по пути: {env_file}")


settings = Settings()
