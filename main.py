from fastapi import FastAPI

app = FastAPI()

galera = {

1:{"nome":"fulano","signo":"libra", "cidade":"guarabira","tipo":"ansioso"},
2:{"nome":"cirrana","signo":"capricórnio","cidade":"sjdc","tipo":"brincalhão"},
3:{"nome":"beltrana","signo":"escorpião","cidade": "rj","tipo":"invocada"},

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


