from fastapi import (
    APIRouter,
    Depends,
    status
)
from fastapi.responses import JSONResponse
from src.core.service.user import (
    UserService,
    get_user_service
)
from src.core.schema.user import (
    UserAddSchema,
    UserResponseSchema,
    UserEditSchema
)
from src.core.service.auth import get_user
from src.conf.log import logger
from uuid import UUID

user: APIRouter = APIRouter(prefix="/user", tags=['User'])


@user.post(
    '/user_add/',
    status_code=status.HTTP_200_OK,
    response_model=UserResponseSchema
)
async def user_add(
        data: UserAddSchema,
        service: UserService = Depends(get_user_service),
        token=Depends(get_user)
):
    return await service.add(account_id=token.id, **data.dict())


@user.get(
    '/user_detail/{id}/',
    status_code=status.HTTP_200_OK,
    response_model=UserResponseSchema
)
async def user_detail(
        _id: UUID,
        service: UserService = Depends(get_user_service),
        token=Depends(get_user)
):
    usr = await service.get_by_id(id=_id)
    return usr


@user.put(
    '/user_edit/{id}/',
    status_code=status.HTTP_202_ACCEPTED,
    response_model=UserResponseSchema
)
async def user_edit(
        _id: UUID,
        data: UserEditSchema,
        service: UserService = Depends(get_user_service)
):
    return await service.update(id=_id, **data.dict())


@user.delete(
    '/user_delete/{id}/',
    status_code=status.HTTP_204_NO_CONTENT,
)
async def user_delete(
        _id: UUID,
        service: UserService = Depends(get_user_service),
        token=Depends(get_user)
):
    await service.h_delete(id=_id)
    return JSONResponse(
        content={
            'detail': "Successful"
        }
    )
