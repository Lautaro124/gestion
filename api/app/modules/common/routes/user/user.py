from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
import uuid
from app.modules.common.core.models.user import UserModelCreated, UserLogin

from app.modules.common.core.schemas.user import User
from app.modules.common.config.dependences import get_db
from app.modules.common.controller.company import get_company_by_id, get_company_by_name
from app.modules.common.controller.type_user import get_type_user_by_id
from app.modules.common.controller.user import create_user, get_user_by_email
from app.modules.common.utils.hash_password import hash_password, verify_password

router = APIRouter()

@router.post('/login')
async def login(
    user: UserLogin = Depends(UserLogin.as_form),
    db: Session = Depends(get_db)
  ):
  try:
    user_db = get_user_by_email(user.email, db)
    if verify_password(user.password, user_db.password):
      return user
    else:
      raise Exception('Unaiuthorized user')
  except Exception as e:
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(e))

@router.post('/')
async def register(
    user: UserModelCreated = Depends(UserModelCreated.as_form),
    db: Session = Depends(get_db),
  ):
  try:
    company = get_company_by_name(user.company_name, db)
    type_user = get_type_user_by_id(user.type_user_id, db)
    hashed_password = hash_password(user.password)
    new_uuid = uuid.uuid4()
    user = User(
      uuid=new_uuid,
      email=user.email,
      password=hashed_password,
      username=user.username,
      company=company,
      type_user=type_user,
      is_superuser=False,
    )
    db_user = create_user(user, db)
    return {
      'uuid': db_user.uuid,
      'email': db_user.email,
      'is_active': db_user.is_active,
      'company_id': db_user.company_id,
      'type_user_id': db_user.type_user_id,
      'username': db_user.username,
    }
  except Exception as e:
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))