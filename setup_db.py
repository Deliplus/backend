# setup_db.py
from db import Base, engine
from models.evaluation import Evaluation
from models.user_progress import UserProgress

print("📦 Creating tables...")
Base.metadata.create_all(bind=engine)
print("✅ Done.")
