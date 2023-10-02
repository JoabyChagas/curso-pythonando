from fastapi import FastAPI

app = FastAPI()

# Comando para rodar o servidor: 
# uvicorn "nome do arquivo sem o .py":app --reload

@app.get("/")
def home():
    x = 10
    for i in range(10):
        x += 1

    return {'mensagem': 'Olá, mundo', 'valor': x}


@app.get('/cadastro')
def cadastro():
    return {'mensagem': 'cadastro'}


@app.get('/login')
def login():
    return {'mensagem': 'login'}

@app.get('/teste/{id}')
def testeid(id):
    return {'valor': id}