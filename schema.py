from pydantic import BaseModel

class userschema(BaseModel):
    id : int
    name : str
    email : str
    nickname : str