from core.configs import settings
from sqlalchemy import Column, Integer, String


class FilmeModel(settings.DBBaseModel):
    __tablename__ = 'filmes'
    
    id: int = Column(Integer, primary_key=True, autoincrement=True)
    titulo: str = Column(String(100))
    duracao: int = Column(Integer)
    
    