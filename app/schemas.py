# app/schemas.py
from pydantic import BaseModel, Field
from typing import Dict

class ChatRequest(BaseModel):
    user_id: str = Field(..., example="u1")
    user_query: str = Field(..., example="Should I invest in gold?")

class ChatResponse(BaseModel):
    intent: str
    reply: str
    next_action: str
    context: Dict = {}

class PurchaseRequest(BaseModel):
    user_id: str = Field(..., example="u1")
    amount_grams: float = Field(..., gt=0, example=1.0)
    payment_method: str = Field(default="wallet", example="wallet")

class PurchaseResponse(BaseModel):
    status: str
    message: str
    purchase_id: str
    details: Dict = {}
