from database import Base, engine
import models  # important : ça importe tes classes User, ClanWar, Bet

print("Creating database...")
Base.metadata.create_all(bind=engine)
print("Done.")
