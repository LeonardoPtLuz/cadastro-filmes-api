from typing import Optional
from pydantic import BaseModel as SCBaseModel

class FilmeSchema(SCBaseModel):
    id: Optional[int]
    titulo: str
    duracao: int
    
    class Config():
        orm_mode = True