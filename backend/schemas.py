from pydantic import BaseModel
from typing import Optional
from datetime import datetime

'''
Ces modèles vont permettre :

de valider les données entrantes (par exemple, quand un utilisateur crée un pari),

de formater les réponses de l’API (ex. transformer un objet SQLAlchemy en JSON).
'''

class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int
    balance: float

    class Config:
        orm_mode = True


class ClanWarBase(BaseModel):
    date: datetime
    clan1: str
    clan2: str

class ClanWarCreate(ClanWarBase):
    pass

class ClanWar(ClanWarBase):
    id: int
    score_clan1: int
    score_clan2: int

    class Config:
        orm_mode = True


class BetBase(BaseModel):
    amount: float
    choice: str

class BetCreate(BetBase):
    user_id: int
    clanwar_id: int

class Bet(BetBase):
    id: int
    user_id: int
    clanwar_id: int

    class Config:
        orm_mode = True
