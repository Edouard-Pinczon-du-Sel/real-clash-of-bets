from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# URL de la base SQLite (elle sera stockée dans un fichier local)
SQLALCHEMY_DATABASE_URL = "sqlite:///./clash.db"

# Création de l'engine
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Création de la session locale
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Classe de base pour nos modèles
Base = declarative_base()
