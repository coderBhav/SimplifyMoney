# app/models.py
from sqlalchemy import Column, String, Float, Integer, DateTime, ForeignKey
from datetime import datetime
from .db import Base

class User(Base):
    __tablename__ = "users"
    user_id = Column(String, primary_key=True, index=True)
    name = Column(String, nullable=True)
    email = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

class SessionState(Base):
    __tablename__ = "sessions"
    user_id = Column(String, ForeignKey("users.user_id"), primary_key=True)
    stage = Column(String, default="start")           # start -> offer -> amount -> ready_to_buy
    fact_index = Column(Integer, default=0)
    amount_pending = Column(Float, nullable=True)
    updated_at = Column(DateTime, default=datetime.utcnow)

class Purchase(Base):
    __tablename__ = "purchases"
    purchase_id = Column(String, primary_key=True, index=True)
    user_id = Column(String, ForeignKey("users.user_id"))
    amount_grams = Column(Float)
    payment_method = Column(String, default="wallet")
    status = Column(String, default="success")
    timestamp = Column(DateTime, default=datetime.utcnow)
