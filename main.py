from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Permitir o painel (GitHub Pages) acessar esta API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

# Banco de dados em memória
db = {
    "convocacoes": [],
    "pads": [],
    "ipms": []
}

@app.get("/")
def home():
    return {"mensagem": "API da Corregedoria Online"}

@app.post("/update")
async def update(payload: dict):
    tipo = payload.get("tipo")

    if tipo not in db:
        return {"erro": "tipo inválido"}

    db[tipo].append(payload)

    return {"status": "ok", "recebido": payload}

@app.get("/dados")
def dados():
    return db
