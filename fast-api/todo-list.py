from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from datetime import date

app = FastAPI() 

# Usando o pydantic para tipar a estrutura de dados da classe
class Todo(BaseModel):
    tarefa: str
    realizada: bool
    prazo: Optional[date]

listaDeTodos = []

@app.post('/inserir') # Adiciona a tarefa recebida à lista de tarefas.
def inserir(todo: Todo):
    try:
        listaDeTodos.append(todo)  
        return {'status': 'sucesso'}
    except:
        return {'status': 'erro'}

@app.post('/listar') # Retorna a lista completa de tarefas
def listar(opcao: int = 0):
    if opcao == 0:
        return listaDeTodos
    elif opcao == 1:
        return list(filter(lambda x: x.realizada == False, listaDeTodos))
    elif opcao == 2:
        return list(filter(lambda x: x.realizada == True, listaDeTodos))

@app.get('/listagemUnica/{id}') # Retorna uma tarefa específica com base no ID.
def listagem(id: int):
    try:
        return listaDeTodos[id]  
    except:
        return {'status': 'tarefa inexistente'}

@app.post('/alterarStatus') # Altera o status de realizada para não realizada e vice-versa.
def alterarStatus(id: int):
    try:
        listaDeTodos[id].realizada = not listaDeTodos[id].realizada
        return {'status': 'sucesso'}
    except:
        return {'status': 'erro'}

@app.post('/excluir') # Remove uma tarefa com base no ID.
def excluir(id: int):
    try:
        del listaDeTodos[id]
        return {'status': 'sucesso'}
    except:
        return {'status': 'erro'}
