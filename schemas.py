from pydantic import BaseModel

class LoginRequest(BaseModel):
    username: str
    password: str

class ProfileInput(BaseModel):
    area_of_interest: str
    strengths: str
    weaknesses: str
