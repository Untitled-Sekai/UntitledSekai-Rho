from pydantic import BaseModel

class UserRegister_Login_Request_Body(BaseModel):
    name: str
    password: str
