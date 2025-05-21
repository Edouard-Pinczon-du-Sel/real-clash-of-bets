from sqlalchemy.orm import Session
import models, schemas


# ----------- Utilisateurs -----------

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(username=user.username, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


# ----------- Clan Wars -----------

def create_clanwar(db: Session, war: schemas.ClanWarCreate):
    db_war = models.ClanWar(**war.dict())
    db.add(db_war)
    db.commit()
    db.refresh(db_war)
    return db_war

def get_clanwars(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.ClanWar).offset(skip).limit(limit).all()


# ----------- Bets -----------

def create_bet(db: Session, bet: schemas.BetCreate):
    db_bet = models.Bet(**bet.dict())
    db.add(db_bet)
    db.commit()
    db.refresh(db_bet)
    return db_bet

def get_bets(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Bet).offset(skip).limit(limit).all()
