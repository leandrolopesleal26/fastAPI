from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

# Rota com retorno de valores
@app.get("/entradas")
async def entradas():
    entradas = {
        'in1' : 0,
        'in2' : 1,
        'in3' : 0,
        'in4' : 0,
        'in5' : 1,
        'in6' : 0,
        'in7' : 1,
        'in8' : 1
    } 
    return entradas

# Com passagem de parametros
@app.get("/entrada/{entrada}") 
async def ler_entrada(entrada):
    print(entrada, type(entrada))
    if entrada == "1":        
        in1 = '0'
        entrada = {'in1': in1} 
    elif entrada == "2":
        in2 = '1'
        entrada = {'in2': in2} 
    else:
        entrada = {'erro': 'Não possui esta entrada'}

    return {"valor da entrada": entrada}