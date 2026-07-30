from fastapi import FastAPI
app =  FastAPI()

@app.get('/')
def ola_mundo():
    return{'mensagem':'Minha primeira API em FastAPI'}