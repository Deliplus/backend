# init_db.py

from db import Base, engine
from models import user_progress, evaluation

print("🔧 Creating database tables...")
Base.metadata.create_all(bind=engine)
print("✅ Done.")
