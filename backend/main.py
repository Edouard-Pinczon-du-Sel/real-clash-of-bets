from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import crud, schemas, db
from typing import List

app = FastAPI()

# Connexion / Déconnexion à la base de données (async)
@app.on_event("startup")
async def startup():
    await db.database.connect()

@app.on_event("shutdown")
async def shutdown():
    await db.database.disconnect()

# Route racine
@app.get("/")
async def root():
    return {"message": "Hello Clash of Bets"}

# Dependency pour la DB session (synchrone avec SQLAlchemy ORM)
def get_db():
    db_session = db.SessionLocal()
    try:
        yield db_session
    finally:
        db_session.close()

# --- ROUTES USERS ---

@app.get("/users/", response_model=List[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_users(db, skip=skip, limit=limit)

@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user)

# --- ROUTES CLANWARS ---

@app.get("/clanwars/", response_model=List[schemas.ClanWar])
def read_clanwars(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_clanwars(db, skip=skip, limit=limit)

@app.post("/clanwars/", response_model=schemas.ClanWar)
def create_clanwar(war: schemas.ClanWarCreate, db: Session = Depends(get_db)):
    return crud.create_clanwar(db, war)

# --- ROUTES BETS ---

@app.get("/bets/", response_model=List[schemas.Bet])
def read_bets(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_bets(db, skip=skip, limit=limit)

@app.post("/bets/", response_model=schemas.Bet)
def create_bet(bet: schemas.BetCreate, db: Session = Depends(get_db)):
    return crud.create_bet(db, bet)
