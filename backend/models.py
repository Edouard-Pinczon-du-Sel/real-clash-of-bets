from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from database import Base  # on importera la Base de database.py

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    balance = Column(Float, default=1000.0)  # argent fictif de départ

    bets = relationship("Bet", back_populates="user")


class ClanWar(Base):
    __tablename__ = "clanwars"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(DateTime)
    clan1 = Column(String)
    clan2 = Column(String)
    score_clan1 = Column(Integer, default=0)
    score_clan2 = Column(Integer, default=0)

    bets = relationship("Bet", back_populates="clanwar")


class Bet(Base):
    __tablename__ = "bets"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    clanwar_id = Column(Integer, ForeignKey("clanwars.id"))
    amount = Column(Float)
    choice = Column(String)  # ex : "clan1" ou "clan2"

    user = relationship("User", back_populates="bets")
    clanwar = relationship("ClanWar", back_populates="bets")
