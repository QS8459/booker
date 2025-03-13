import jwt
from jwt import (
    InvalidTokenError,
    InvalidSignatureError
)
from datetime import datetime, timezone, timedelta
from fastapi.security.oauth2 import OAuth2PasswordBearer
from fastapi import (
    Depends,
    HTTPException,
    status
)
from src.conf.settings import settings
from src.conf.log import logger
from src.core.schema.account import AccountResponseSchema

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='api/v1/account/login/', scheme_name='jwt')


async def get_user(
        token: str = Depends(oauth2_scheme)
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, settings.secret_key, settings.token_crypt_algorithm)
        username = payload.get('username')
        if username is None:
            raise credentials_exception
        exp_date = payload.get('exp')
        time_diff = (datetime.now(timezone.utc).timestamp() - exp_date) / 60
        if 0 < time_diff < 30:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail='Token Expired',
                headers={"WWW-Authenticate": "Bearer"}
            )
        return AccountResponseSchema(
            id=payload.get('id'),
            email=username,
            role=payload.get('role')
        )
    except (InvalidTokenError, InvalidSignatureError) as e:
        logger.error(e)

        raise credentials_exception


async def get_admin(
    current_user=Depends(get_user)
):
    logger.info(current_user)
    if current_user.role == "ADMIN":
        return current_user
    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="Permission Denied",
    )


async def get_vendor(
        current_user=Depends(oauth2_scheme)
):
    if current_user.role != "VENDOR" and current_user.role != "ADMIN":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Permission Denied"
        )
    return current_user

def generate_token(data: dict = None):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=settings.token_exp_time_min)
    to_encode.update({'exp': expire})

    return jwt.encode(
        payload=to_encode,
        key=settings.secret_key,
        algorithm=settings.token_crypt_algorithm
    )
