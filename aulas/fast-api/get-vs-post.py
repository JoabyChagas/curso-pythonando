from fastapi import FastAPI

app = FastAPI()

usuarios = [(1, 'Joaby', 'Chagas'), (2, 'Juma', 'Tainá'), (3, 'Luiz', 'Mario')]

# O método GET é usado para recuperar (ou ler) dados do servidor, é ideal para consultas de dados.
@app.get('/usuario/{id}') # <--- url
def usuarioGet(id: int):
    for i in usuarios:
        if i[0] == id:
            return i
    return 'Não existe esse usuário'


# O método POST é mais adequado quando a intenção é modificar o estado do servidor, como criar, atualizar ou excluir recursos.
@app.post('/usuario')
def usuarioPost(id: int): # <--- parâmetro
    for i in usuarios:
        if i[0] == id:
            return i
    return 'Não existe esse usuário'