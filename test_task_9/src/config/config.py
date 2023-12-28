from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class PostgresSettings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env.db_example', env_file_encoding='utf-8')

    host: str = Field(alias='POSTGRES_HOST')
    port: int = Field(alias='POSTGRES_PORT')
    user: str = Field(alias='POSTGRES_USER')
    password: str = Field(alias='POSTGRES_PASSWORD')
    db: str = Field(alias='POSTGRES_DB')

    @property
    def get_uri(self):
        return 'postgresql+asyncpg://{}:{}@{}:{}/{}'.format(
            self.user,
            self.password,
            self.host,
            self.port,
            self.db
        )


class AppSettings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env.app_example', env_file_encoding='utf-8')

    name: str = Field(alias='NAME_PROJECT')


class Settings:
    postgres: PostgresSettings = PostgresSettings()
    app: AppSettings = AppSettings()


settings = Settings()
