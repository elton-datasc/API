from fastapi import FastAPI
#python -m uvicorn main:app --reload


description = """
Demonstrativo de vendas mensais por produto.

## Itens

Itens **somente para consulta**.

## Usuários

Estão aptos:

* **Baixar arquivos** (_implementado_).
* **Realizar consultas** (_implementado_).
"""

app = FastAPI(
    title="Vendas mensais",
    description=description,
    version="0.0.1",
    terms_of_service="http://example.com/terms/",
    contact={
        "name": "Elton Guilherme de Almeida",
        "url": "https://www.linkedin.com/in/elton-guilherme/",
        "email": "elton_guilherme_dsc@hotmail.com",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
        
    },
)

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