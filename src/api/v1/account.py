from fastapi import (
    APIRouter,
    Depends,
    Form,
    status
)
from src.core.service.account import (
    AccountService,
    get_account_service
)
from src.core.schema.token import TokenResponseSchema
from src.core.schema.account import (
    AccountCreateSchema,
    AccountResponseSchema
)
from src.core.service.auth import generate_token, get_user

account: APIRouter = APIRouter(prefix="/account", tags=['Account'])


@account.get('/', status_code=status.HTTP_200_OK)
async def account_home(
        service: AccountService = Depends(get_account_service)
):
    return "Hello From the Account"


@account.post(
    '/sign_up/',
    status_code=status.HTTP_201_CREATED,
    response_model=AccountResponseSchema
)
async def add_account(
        data: AccountCreateSchema,
        service: AccountService = Depends(get_account_service)
):
    return await service.add(**data.dict())


@account.post(
    '/login/',
    status_code=status.HTTP_200_OK,
    response_model=TokenResponseSchema
)
async def login(
    username: str = Form(...),
    password: str = Form(...),
    service: AccountService = Depends(get_account_service)
):
    user = await service.authenticate(email=username, password=password)
    if user:
        token = generate_token({
            'username': user.get('email'),
            'id': f'{user.get("id")}'
        }
        )
        return TokenResponseSchema(
            access_token=token,
            token_type='bearer'
        )
    return None


@account.get(
    '/me/',
    status_code=status.HTTP_200_OK,
    response_model=AccountResponseSchema
)
async def me(
        token=Depends(get_user),
        service: AccountService = Depends(get_account_service)
):
    user = await service.get_by_email(token)
    return user
