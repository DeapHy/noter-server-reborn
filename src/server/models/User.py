from pydantic import BaseModel

class AuthUserModel(BaseModel):
    login: str
    salt: str
    password_hash: str
    display_name: str

class UserModel(BaseModel):
    userID: str
    display_name: str