from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from db import SessionLocal
from models import User
from schemas import LoginRequest, ProfileInput
from llm_client import query_llama
import bcrypt

router = APIRouter()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/login")
def login(request: LoginRequest, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == request.username).first()
    if user and bcrypt.checkpw(request.password.encode(), user.password.encode()):
        return {"message": "Login successful!"}
    raise HTTPException(status_code=401, detail="Invalid credentials")

@router.post("/submit-profile")
def submit_profile(input: ProfileInput):
    prompt = f"""
    Analyze the following user profile:
    Area of Interest: {input.area_of_interest}
    Strengths: {input.strengths}
    Weaknesses: {input.weaknesses}
    
    Provide constructive feedback and career suggestions.
    """
    ai_response = query_llama(prompt)
    return {"analysis": ai_response}

