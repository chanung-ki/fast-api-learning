from sqlalchemy.orm import Session

import user_schema
from models import User

def insert(db: Session, _userObj: user_schema.User):
    # pydantiv v1
    # customer = _userObj.dict(exclude_unset=True)
    # pydantiv v2
    user = _userObj.model_dump(exclude_unset=True)

    db_user = User(**user)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user.seq

