from sqlalchemy import Column, Integer, String, Enum
from api.v1.user.user_schema import GenderType

from database import Base

class User(Base):
    __tablename__ = "USER"

    req = Column(Integer, primary_key=True, index=True)
    name = Column(String(10), nullable=False)  # min_length=1, max_length=10 이 SQLAlchemy의 length로 설정됨
    phone = Column(String, nullable=False)  # 전화번호를 저장하는 컬럼
    gender = Column(Enum(GenderType), nullable=False)  # GenderType을 Enum으로 설정
    birth = Column(String, nullable=True)  # Optional한 birth 컬럼

    def __repr__(self):
        return f"User(id={self.req}, name={self.name}, phone={self.phone}, gender={self.gender}, birth={self.birth})"