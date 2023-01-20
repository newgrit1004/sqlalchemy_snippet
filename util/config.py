from pathlib import Path

from pydantic import BaseSettings


class Setting(BaseSettings):
    """Setting Configuration"""
    testdb_uri: str
    timezone: str

    class Config:
        case_sensitive = True
        env_file = Path(__file__).parent / ".env"


setting = Setting()