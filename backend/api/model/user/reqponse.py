from ..response import ResponseModel

class UserRegisterResponse(ResponseModel):
    success: bool = True
    message: str = "Register successfully | 登録成功"

class UserLoginResponse(ResponseModel):
    success: bool = True
    message: str = "Login successfully | ログイン成功"