# backend/models/evaluation.py

from sqlalchemy import Column, Integer, String, DateTime, Text
from datetime import datetime
from db import Base


class Evaluation(Base):
    __tablename__ = "evaluations"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, nullable=False)
    source_text = Column(Text, nullable=False)
    chosen_id = Column(String, nullable=False)
    adequacy = Column(Integer)
    fluency = Column(Integer)
    timestamp = Column(DateTime, default=datetime.utcnow)
