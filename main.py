from fastapi import FastAPI

app = FastAPI()

galera = {

1:{"nome":"elton","signo":"libra", "cidade":"joão pessoa","tipo":"ansioso"},
2:{"nome":"lu","signo":"capricórnio","cidade":"sjdc","tipo":"radical livre"},
3:{"nome":"raye","signo":"escorpião","cidade": "rio de janeiro","tipo":"teimosinha"},

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

