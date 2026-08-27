from pydantic import BaseModel

class ProdutoBase(BaseModel):
    nome: str
    preco: float
    quantidade: int

class ProdutoCreate(ProdutoBase):
    pass

class ProdutoResponse(ProdutoBase):
    id: int

class Config:
    from_attributes = True 

class LivroBase(BaseModel):
    titulo: str
    autor: str
    ano_publicacao: int
    preco: float
    quantidade: int

class LivroCreate(LivroBase):
    pass

class LivroResponse(LivroBase):
    id: int

class Config:
    from_attributes = True 