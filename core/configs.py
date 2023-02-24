from typing import List
from pydantic import BaseSettings, AnyHttpUrl
from sqlalchemy.ext.declarative import declarative_base

class Settings(BaseSettings):
    API_V1_STR = '/api/v1'
    DB_URL = 'postgresql+asyncpg://leo:123456@localhost:5432/filmescadastro'
    DBBaseModel = declarative_base()
    
    class Config():
        case_sensitive = True
        #orm_mode = True
        
settings = Settings()