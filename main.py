from fastapi import FastAPI

app = FastAPI()

galera = {

1:{"produto":"refrigerante 2l","un":"garrafa", "area":"padaria","tipo":"bebida"},
2:{"produto":"refrigerante lata","un":"lt","area":"padaria","tipo":"bebida"},
3:{"produto":"pão de caixa","un":"un","area": "padaria","tipo":"pao"},
4:{"produto":"catchup","un":"bisnaga", "area":"condimentos","tipo":""},
5:{"produto":"mostarda","un":"bisnaga","area":"condimentos","tipo":""},
6:{"produto":"maionese","un":"bisnaga","area": "condimentos","tipo":""},
7:{"produto":"tomate","un":"kg", "area":"hortifruti","tipo":"legume"},
8:{"produto":"laranja","un":"kg","area":"hortifruti","tipo":"fruta"},
9:{"produto":"banana","un":"kg","area": "hortifruti","tipo":"fruta"},

}

#criando as rotas

@app.get("/galera")
def pessoas():
  return galera


@app.get("/galera/{id}")
def filtro_pessoas(id: int):
  return galera[id]
  

@app.get("/")
def contagem_de_pessoas():
  return {"galera" : len(galera)}


