from sqlalchemy import BigInteger, Column, String
from tg_bot.core import Loader

# Example


class Users(Loader.Base):
    __tablename__ = "users"

    id = Column(BigInteger, primary_key=True)
    full_name = Column(String(150))
    username = Column(String(150))
