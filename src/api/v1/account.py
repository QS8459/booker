from fastapi import (
    APIRouter,
    Depends,
    Form,
    Query,
    status
)
from src.core.service.account import (
    AccountService,
    get_account_service
)
from src.core.schema.token import TokenResponseSchema
from src.core.schema.account import (
    AccountAddSchema,
    AccountResponseSchema
)
from src.core.service.auth import (
    generate_token, get_user,
    get_admin
)
from src.core.schema.response import ResponseBaseSchema
from src.conf.log import logger

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
        data: AccountAddSchema,
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
            'id': f'{user.get("id")}',
            'role': user.get('role')
        }
        )
        return TokenResponseSchema(
            access_token=token,
            token_type='bearer'
        )
    return None


@account.get(
    '/list/',
    status_code=status.HTTP_200_OK,
    response_model=ResponseBaseSchema
)
async def user_list(
        page: int = Query(default=1),
        page_size: int = Query(default=10),
        service: AccountService = Depends(get_account_service),
        token=Depends(get_admin)
):
    count = await service.get_count()
    data_list = await service.get_all(offset=page-1, limit=page_size)
    return ResponseBaseSchema[AccountResponseSchema](
        count=count[0],
        result=data_list
    )


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


@account.post(
    '/add_vendor/',
    status_code=status.HTTP_201_CREATED,
    response_model=AccountResponseSchema
)
async def add_vendor(
        data: AccountAddSchema,
        service: AccountService = Depends(get_account_service),
        admin=Depends(get_admin)
):
    data.role="VENDOR"
    return await service.add(**data.dict())

#
# @account.post(
#     '/new_admin/',
#     status_code=status.HTTP_201_CREATED,
#     response_model=AccountResponseSchema
# )
# async def add_vendor(
#         data: AccountAddSchema,
#         service: AccountService = Depends(get_account_service),
# ):
#     data.role="ADMIN"
#     return await service.add(**data.dict())