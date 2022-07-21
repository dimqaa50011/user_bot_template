from pydantic import BaseModel


class CoreBot(BaseModel):
    api_id: int
    api_hash: str


class DbConfig(BaseModel):
    user: str
    password: str
    database: str
    host: str
    
class Misk(BaseModel):
    other: str = None
