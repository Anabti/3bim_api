from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import Base, engine, get_db
from models import ProdutoDB
from schemas import ProdutoCreate, ProdutoResponse
from models import LivroDB
from schemas import LivroCreate, LivroResponse
from fastapi import HTTPException



from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine) # cria as tabelas, se ainda não existirem
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    # em produção, restringir para o domínio real do front-end
    allow_methods=['*'],
    allow_headers=['*'],
    )

# GET /produtos/{id} -> retorna um único produto pelo id
@app.get('/produtos/{produto_id}', response_model=ProdutoResponse)
def obter_produto(produto_id: int, db: Session = Depends(get_db)):
    produto = db.query(ProdutoDB).filter(ProdutoDB.id == produto_id).first()
    if produto is None:
        raise HTTPException(status_code=404, detail='Produto não encontrado')
        return produto

# DELETE /produtos/{id} -> remove um produto do banco de dados
@app.delete('/produtos/{produto_id}', status_code=204)
def remover_produto(produto_id: int, db: Session = Depends(get_db)):
    produto = db.query(ProdutoDB).filter(ProdutoDB.id == produto_id).first()
    if produto is None:
        raise HTTPException(status_code=404, detail='Produto não encontrado')
    db.delete(produto)
    db.commit()

@app.get('/produtos', response_model=list[ProdutoResponse])
def listar_produtos(db: Session = Depends(get_db)):
    return db.query(ProdutoDB).all()
    
@app.post('/produtos', response_model=ProdutoResponse, status_code=201)
def criar_produto(produto: ProdutoCreate, db: Session = Depends(get_db)):
    novo_produto = ProdutoDB(**produto.dict())
    db.add(novo_produto)
    db.commit()
    db.refresh(novo_produto)
    return novo_produto

# PUT /produtos/{id} -> atualiza um produto existente no banco
@app.put('/produtos/{produto_id}', response_model=ProdutoResponse)
def atualizar_produto(produto_id: int, dados: ProdutoCreate, db:
    Session = Depends(get_db)):
        produto = db.query(ProdutoDB).filter(ProdutoDB.id == produto_id).first()
        if produto is None:
            raise HTTPException(status_code=404, detail='Produto não encontrado')
        produto.nome = dados.nome
        produto.preco = dados.preco
        produto.quantidade = dados.quantidade
        db.commit()
        db.refresh(produto)
        return produto

#Livros

# GET /livro/{id} -> retorna um único livro pelo id
@app.get('/livro /{livro _id}', response_model=LivroResponse)
def obter_livro (livro_id: int, db: Session = Depends(get_db)):
    livro  = db.query(LivroDB).filter(LivroDB.id == livro_id).first()
    if livro  is None:
        raise HTTPException(status_code=404, detail='Livro não encontrado')
        return livro 

# DELETE /livro /{id} -> remove um livro  do banco de dados
@app.delete('/livro /{produto_id}', status_code=204)
def remover_livro (produto_id: int, db: Session = Depends(get_db)):
    livro = db.query(LivroivroDB).filter(LivroDB.id == livro_id).first()
    if livro  is None:
        raise HTTPException(status_code=404, detail='Livro  não encontrado')
    db.delete(livro)
    db.commit()

@app.get('/livro ', response_model=list[LivroResponse])
def listar_livro (db: Session = Depends(get_db)):
    return db.query(Livro DB).all()
    
@app.post('/livro ', response_model=LivroResponse, status_code=201)
def criar_livro (livro: LivroCreate, db: Session = Depends(get_db)):
    novo_livro  = LivroDB(**livro.dict())
    db.add(novo_livro )
    db.commit()
    db.refresh(novo_livro )
    return novo_livro 

# PUT /livro/{id} -> atualiza um livro existente no banco
@app.put('/livro/{livro_id}', response_model=LivroResponse)
def atualizar_livro(livro_id: int, dados: LivroCreate, db:
    Session = Depends(get_db)):
        livro = db.query(LivroDB).filter(LivroDB.id == livro_id).first()
        if livro is None:
            raise HTTPException(status_code=404, detail='Livro não encontrado')
        livro.titulo = dados.titulo
        livro.autor = dados.autor
        livro.ano_publicacao = dados.ano_publicacao
        livro.quantidade = dados.quantidade
        livro.preco = dados.preco
        db.commit()
        db.refresh(livro)
        return livro

