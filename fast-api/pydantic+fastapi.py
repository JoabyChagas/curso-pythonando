from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Criamos uma classe Pydantic para definir a estrutura dos dados do usuário
class Usuario(BaseModel):
    id: int
    nome: str
    sobrenome: str

# lista de usuários
usuarios = [
    Usuario(id=1, nome='Joaby', sobrenome='Chagas'),
    Usuario(id=2, nome='Juma', sobrenome='Tainá'),
    Usuario(id=3, nome='Luiz', sobrenome='Mario'),
]

# Rota GET para obter a lista de usuários
@app.get('/usuarioLista')
def usuario_get():
    return usuarios

# Rota POST para adicionar um novo usuário
@app.post('/usuario')
def usuario_post(usuario: Usuario):
    usuarios.append(usuario)
    return 'usuário cadastrado'
