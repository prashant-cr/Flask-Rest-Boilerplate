from sqlalchemy import Column, ForeignKey, String, TIMESTAMP, text, JSON, DateTime
from sqlalchemy.dialects.mysql import INTEGER, TINYINT, ENUM, BIGINT
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class BankTable(Base):

    __tablename__ = 'bank'

    id = Column(INTEGER(11), primary_key=True, autoincrement=True)
    name = Column(String(255))
    address = Column(String(1000))
    mobile_number = Column(INTEGER(11))
    bank_manager = Column(String(500))
    is_deleted = Column(TINYINT(1), server_default=text("'0'"))
    created_on = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    modified_on = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class BranchTable(Base):

    __tablename__ = 'branch_info'

    id = Column(INTEGER(11), primary_key=True, autoincrement=True)
    address = Column(String(1000))
    mobile_number = Column(INTEGER(11))
    branch_manager = Column(String(255))
    is_deleted = Column(TINYINT(1), server_default=text("'0'"))
    created_on = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    modified_on = Column(TIMESTAMP, nullable=False,
                         server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
