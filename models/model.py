from sqlalchemy import Column, ForeignKey, String, TIMESTAMP, text, JSON, DateTime
from sqlalchemy.dialects.mysql import INTEGER, TINYINT, ENUM, BIGINT
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class BankTable(Base):

    __tablename__ = 'Bank'

    id = Column(INTEGER(11), primary_key=True)
    title = Column(String(255))
    created_on = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    modified_on = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))

