from turtle import pu
from fastapi import FastAPI

app = FastAPI()

vendas = {

1:{"produto":"refrigerante 2l","un":"garrafa", "area":"padaria","tipo":"bebida","pu":3.8},
2:{"produto":"refrigerante lata","un":"lt","area":"padaria","tipo":"bebida", "pu":1.5},
3:{"produto":"pão de caixa","un":"un","area": "padaria","tipo":"pao","pu":2.},
4:{"produto":"catchup","un":"bisnaga", "area":"condimentos","tipo":"","pu":3.},
5:{"produto":"mostarda","un":"bisnaga","area":"condimentos","tipo":"","pu":1.6},
6:{"produto":"maionese","un":"bisnaga","area": "condimentos","tipo":"","pu":2.5},
7:{"produto":"tomate","un":"kg", "area":"hortifruti","tipo":"legume","pu":.8},
8:{"produto":"laranja","un":"kg","area":"hortifruti","tipo":"fruta","pu":1.1},
9:{"produto":"banana","un":"kg","area": "hortifruti","tipo":"fruta","pu":3.8},

}

#criando as rotas

@app.get("/vendas")
def produtos_vendidos():
  return vendas


@app.get("/vendas/{id}")
def filtro_vendas_id(id: int):
  return vendas[id]
  

@app.get("/soma_vendas")
def vendas_totais():
  l = [vendas[i]['pu'] for i in vendas]
  i = [v for i, v in enumerate(vendas)]
  return {"qtde de vendas" : len(i),"vendas totais" : sum(l)}

@app.get("/openapi.json")
def schema():
  return schema