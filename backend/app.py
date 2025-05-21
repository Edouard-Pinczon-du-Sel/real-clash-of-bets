from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Bienvenue sur Clash of Bets Backend"}
