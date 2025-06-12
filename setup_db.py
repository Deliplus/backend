# setup_db.py

from db import Base, engine
from models.evaluation import Evaluation  # absolute import
from db import engine

Base.metadata.create_all(bind=engine)
print("✅ Tables created.")
