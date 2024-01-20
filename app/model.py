from sqlalchemy import TIMESTAMP, Column, Integer, LargeBinary, String, text
from sqlalchemy.sql import func

from .database import Base


class Posts(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    date_created = Column(TIMESTAMP, server_default=func.now())
    last_modifies = Column(
        TIMESTAMP, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP")
    )
    views = Column(Integer, default=0)
    tags = Column(String)
    iamge = Column(LargeBinary)
